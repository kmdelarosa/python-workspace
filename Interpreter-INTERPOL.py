DINT,DST,STORE,PRINT,PRINTN,INPUTN,USERINPUT,OUTPUT = "DINT","DSTR","STORE","GIVEYOU!","GIVEYOU!!","GIVEME?","USER_INPUT","OUTPUT"
DECLARATION_INT,DECLARATION_STR = "DECLARATION_INTEGER","DECLARATION_STRING"
PLUS,MINUS,MULT,DIV,MODU = "PLUS","MINUS","MULT","DIV","MODU"
EXPO,ROOT,MEAN,DISTANCE = "RAISE","ROOT","MEAN","DIST"
OPERATION,VARIABLE,INTEGER,STRING,IDENTIFIER,EXPRESSION = "OPERATION","VARIABLE","INTEGER","STRING","IDENTIFIER","EXPRESSION"
ASSIGNMENT,DEC_ASSIGNMENT,VAR_ASSIGNMENT,DECLARATION_ASSIGNMENT, VARIABLE_ASSIGNMENT = "ASSIGNMENT","WITH","IN","DECLARATION_ASSIGNMENT","VARIABLE_ASSIGNMENT"

class Token(object):
    def __init__(self,type,value):
        self.type = type
        self.value = value

    def __str__(self):
        return 'Token({type},{value})'.format(type = self.type, value = repr(self.value))

    def __repr__(self):
        return self.__str__()

class InputOutput(object):
    def __init__(self):
        self = self

    def inputSourceFile(self):
        return input("Input source file: ")   

    def inputFromUser(self):
        # Asking input from the user:  GIVEME? <variable_name>
        return input("GIVEME? ") 

    def printOutput(self,tag,output_block):
        if tag == 1:
            # Printing values, variables, and expressions: GIVEYOU! <expression>
            return print(output_block)
        elif tag == 2:
            # Printing values, variables, and expressions with a new line affixed at the end: GIVEYOU!! <expression>
            return print(output_block,"\n")

    def readIpolFile(self,ipol_file):
    # read indicated .ipol file
        code = []
        
        try:
            file = open(ipol_file,"r")
            
        except IOError:
            print("ERROR! FILE DOES NOT EXIST!")

        for line in file:
            code.append(line.rstrip())
        file.close()

        return code

    def checkIpolFile(self,ipol_file):
    # verifies if .ipol file is valid
        import os.path

        if(len(ipol_file.split(".")) <= 1 or ipol_file.split(".")[1] != "ipol"):
            return "INVALID SOURCE FILE!"
        #check if file exists
        elif os.path.exists(ipol_file) != True:
            return "INVALID SOURCE FILE!"
        else:
            return ipol_file

class ArithmeticOperations(object):
    import math

    def __init__(self,arith_values):
        self = self
        self.arith_values = arith_values
    
    def add(self,val1,val2):
        # Addition: PLUS <expression1> <expression2>
        return val1+val2
    
    def sub(self,val1,val2):
        # Subtraction: MINUS <expression1> <expression2>
        return val1-val2
    
    def mul(self,val1,val2):
        # Multiplication: TIMES <expression1> <expression2>
        return val1*val2
    
    def div(self,val1,val2):
        # Division: DIVBY <expression1> <expression2>
        return val1/val2
    
    def mod(self,val1,val2):
        # Modulo: MODU <expression1> <expression2>
        return val1%val2

class AdvancedArithmetic(ArithmeticOperations):
    def __init__(self):
        self = self
    
    def exp(self,expr,expo):
        # Exponentiation: RAISE <expression> <exponent>
        return expr**expo

    def nthRoot(self,N,expr):
        # Nth Root of a No. : ROOT <N> <expression>
        # add formula here
        return expr

    def avg(self,values):
        # Average: MEAN <expr1> <expr2> <expr3> … <exprn>
        #  This is the only operation that accepts an unlimited number of parameters.
        sum = 0
        for value in values:
            sum += value
        
        avg = sum/len(values)
        
        return avg 

    def distance(self,pt1,pt2):
        # Distance between two points: DIST <expr1> <expr2> AND <expr3> <expr4>
        # #  The 2 points are separated by ‘AND’
        # #  The coordinates of the first point are <expression1> and <expression2> 
        # #  The coordinates of the second point are <expression3> and <expression4>
        return (pt2[1]-pt1[1])+(pt2[0]-pt1[0])

# InterpolBody is for the processing of the entire code block
class InterpolBody(object):

    def __init__(self,code_block,syntax_status,parse_status):
        self = self
        self.code_block = code_block
        self.syntax_status = syntax_status
        self.parse_status = parse_status
    
    def processBlock(self):

        input_output = InputOutput()
        operations = ArithmeticOperations(self)
        adv_operations = AdvancedArithmetic()

        temp_tokens = []
        temp_symb_table = []
        variables = []
        all_symb_table = []
        all_variables = []
        errors = -1

        syntax_errors = 0
        grammar_errors = 0

        for i in range(len(self.code_block)):
            
            # split code line by spaces
            temp_tokens = self.code_block[i].replace('\t','').split(' ')

            if temp_tokens == "CREATE":
                    errors += 1
                    print("SYNTAX ERROR!")
                    break
            
            elif temp_tokens == "RUPTURE":
                break
            
            else:
                strng_index = -1

                for i in range(len(temp_tokens)):

                    if temp_tokens[i].find("[") != -1:
                        strng_index = i
                        
                        for strng in temp_tokens[i+1:]:
                            if strng.find("[") != -1:
                                print("INVALID SYNTAX ERROR!")
                                break
                            else:
                                temp_tokens[i] = temp_tokens[i] + " " + strng
                                if(strng.find("]") != -1):
                                    break
                    i+=1

                if strng_index != -1:
                    del temp_tokens[strng_index+1:]

                # check syntax: lexical analysis
                
                print(temp_tokens)

                temp_symb_table,syntax_errors = self.checkSyntax(temp_tokens)
                all_symb_table.append(temp_symb_table)
                    
                grammar_errors = self.checkGrammar(temp_symb_table,all_variables)

                if len(temp_symb_table) == 2 and (temp_symb_table[0].type == OUTPUT or temp_symb_table[0].type == PRINTN):
                    if self.checkAllVariables(temp_symb_table[1],all_variables) == False and temp_symb_table[0].value == PRINT:
                        input_output.printOutput(1, self.retrieveFromVariables(temp_symb_table[1],all_variables))
                    elif self.checkAllVariables(temp_symb_table[1],all_variables) == False and temp_symb_table[0].value == PRINTN:
                        input_output.printOutput(2, self.retrieveFromVariables(temp_symb_table[1],all_variables))
                
                print("errors",grammar_errors)
                if grammar_errors > 0:
                    break

        print("LEXEMES AND TOKENS TABLE") 
        line_count = 0   
        for each_token_set in all_symb_table:
            for each_token in each_token_set:
                print("["+str(line_count)+"]",each_token.type,each_token.value,sep = "\t\t")
            line_count += 1
        
        print("SYMBOL TABLE")
        for variable in all_variables:
            print(variable[1],variable[0],variable[2],sep="\t")

    def checkSyntax(self,block_line):

        symbol_table = []
        
        isDeclaration = False
        isAssignment = False

        startToken = 0
        token_type = ""

        errors = 0

        for i in range(len(block_line)):
            # check if declaration
            # check type of declaration

            if block_line[i] == DINT and i==0:
                
                isDeclaration = True
                startToken = 1
                token_type = DECLARATION_INT
                #self.syntax_status = True
            
            elif block_line[i] == DST and i==0:
                isDeclaration = True
                startToken = 1
                token_type = DECLARATION_STR

            elif block_line[i] == STORE and i==0:
                
                isAssignment = True
                startToken = 1
                token_type = ASSIGNMENT
                #self.syntax_status = True  
               
            elif isinstance(block_line[i],int):
                
                token_type = INTEGER
                #self.syntax_status = True
            
            elif block_line[i] == DEC_ASSIGNMENT:
                token_type = DECLARATION_ASSIGNMENT
                #self.syntax_status = True
            
            elif block_line[i] == VAR_ASSIGNMENT:
                token_type = VARIABLE_ASSIGNMENT

            elif block_line[i] == PLUS or block_line[i] == MINUS or block_line[i] == DIV or block_line[i] == MULT or block_line[i] == DIV or block_line[i] == MODU:
                
                token_type = OPERATION
                #self.syntax_status = True

            elif block_line[i].find("[") != -1 or block_line[i].find("]") != -1:
                
                token_type = STRING
                self.syntax_status = True
            
            elif block_line[i] == PRINT:
                token_type = OUTPUT
               # self.syntax_status = True
            
            elif block_line[i] == PRINTN:
                token_type = OUTPUT
                #self.syntax_status = True
            
            elif block_line[i] == INPUTN:
                token_type = USERINPUT
            
            elif block_line[i].isdigit() == True:
                token_type = INTEGER

            else:
                token_type = VARIABLE
            
            if token_type == "":
                errors += 1
            else:
                symbol_table.append(Token(token_type,block_line[i]))
            
            token_type = ""
            i+=1

        return symbol_table,errors


    def checkGrammar(self,block_line,all_variables):

        # check grammar of code block
        # code block is broken down into symbol table
        # check if arrangement of tokens are valid

        isDeclaration = 0
        isAssignment = 0
        isVarInput = 0
        isPrint = 0

        hasWith, hasIn = 0,0

        expression_start,expression_end = 0,0
        temp_expression = []
        expressions = []

        variables = []
        eval_result = 0

        isValidOperation = False

        declarationType = ""

        errors = 0
        token_count = 0

        for token in block_line:

            # for each token in a line
            if token.type == DECLARATION_INT and token_count == 0:
                isDeclaration = 1
                expression_start = 1
                declarationType = "int"
            
            elif token.type == DECLARATION_STR and token_count == 0:
                isDeclaration = 1
                expression_start = 1
                declarationType = "string"
            
            elif token.type == ASSIGNMENT and token_count == 0:
                isAssignment = 1
            
            elif token.type == DECLARATION_ASSIGNMENT:
                # check if "WITH" and count == 2
                # should have a variable before and declaration
                if isDeclaration == 1 and isAssignment == 0:
                    expression_end = 1
                    hasWith = 1
                    expressions.append(temp_expression)
                    #evaluate expression
                    eval_result = self.evaluateExpression(errors,all_variables,temp_expression)
                    temp_expression =[]

            elif token.type == VARIABLE_ASSIGNMENT:
                # check if "IN"
                # should be assignment (store) and expression before
                if isAssignment == 1 and isDeclaration == 0:
                    expression_end = token_count
                    hasIn = 1
                    expressions.append(temp_expression)
                    #evaluate expression
                    eval_result = self.evaluateExpression(errors,all_variables,temp_expression)
                    temp_expression =[]

            elif token.type == OUTPUT and token_count == 0:
                # print value of following variable
                isPrint = 1
            
            elif token.type == USERINPUT and token_count == 0:
                isVarInput = 1
            
            elif token.type == VARIABLE and isVarInput == 1 and isAssignment == 0 and isDeclaration == 0:
                all_variables.append([STRING,token.value,"-"])
            
            elif isDeclaration == 1 and isPrint == 0 and isAssignment == 0 and token.type != DECLARATION_ASSIGNMENT and token.type != VARIABLE_ASSIGNMENT:
                #should read in an expression
                #if expression_end != 1 and expression_start == 1:
                if token.type == VARIABLE and declarationType == "int" and self.checkAllVariables(token,all_variables) == False :
                    all_variables.append([INTEGER,token.value,-1])
                elif token.type == VARIABLE and declarationType == "string" and self.checkAllVariables(token,all_variables) == False:
                    all_variables.append([STRING,token.value,"-"])

                temp_expression.append(token)
            elif (isAssignment == 1 and isPrint == 0 and isDeclaration == 0 and token.type != VARIABLE_ASSIGNMENT and token.type != DECLARATION_ASSIGNMENT) or (isVarInput == 1 and isDeclaration == 0 and isAssignment == 0 and token.type != VARIABLE_ASSIGNMENT and token.type != DECLARATION_ASSIGNMENT):
                #should read in an expression
                #if expression_end != 1 and expression_start == 1:
                #check in list of all variables if existing
                if token.type == VARIABLE and self.checkAllVariables(token,all_variables) == False:
                    # assigns eval result variable with -1 value (default value for integer) 
                    count = 0
                    for var in all_variables:
                        if var[1] == token.value and var[2] == -1:
                            all_variables[count][2] = eval_result
                        count += 1
                            
                temp_expression.append(token)
            
            elif isPrint == 1 and isDeclaration == 0 and isAssignment == 0 and token.type != DECLARATION_ASSIGNMENT and token.type != VARIABLE_ASSIGNMENT:
                #should read in an expression
                if self.checkAllVariables(token,all_variables) == False and self.retrieveFromVariables(token,all_variables) == token.value:
                    errors+=1

                temp_expression.append(token)
            else:
                errors += 1

            token_count += 1
        expressions.append(temp_expression)
        eval_result = self.evaluateExpression(errors,all_variables,temp_expression)

        if isDeclaration == 1 and isPrint == 0 and isAssignment == 0 and token.type != DECLARATION_ASSIGNMENT and token.type != VARIABLE_ASSIGNMENT and hasWith == 1:
            # works for code blocks with only 1 variable
            all_variables[len(all_variables)-1][2] = eval_result
        
        print(errors,token)

        return errors
    
    def checkAllVariables(self,variable,variables):
        for var in variables:
            if var[1] == variable.value and var[0] == variable.type:
                return True
        return False
    
    def retrieveFromVariables(self,variable,variables):
        for var in variables:
            if var[1] == variable.value:
                return var[2]
        return variable.value
    
    def checkSucceedingElements(self,expression,count,variables):
        index = 0
        variable_flag = 0
        variables = []

        for element in expression:
            if element.type == VARIABLE:
                variable_flag += 1
                variables.append([index,element])
            index += 1
        
        if variable_flag == 0:
            # if all succeeding elements are integers
            return 0
                    
        else:
            # if there are any non-integer (variable)
            for elem in variables:
                if self.checkAllVariables(elem[1].value,variables) == True:
                    expression[elem[0]].value = self.retrieveFromVariables(expression[elem[0]].value,variables)


    def evaluateExpression(self,errors,variables,expression):
        operations = ArithmeticOperations([])
        adv_operations = AdvancedArithmetic()
        
        while len(expression) > 3:
        
            count,start,end = 0,0,0
            
            for element in expression:
                if element.type == OPERATION: # if operation is for 2 digit operation
                    start,end = count,count+2
                    if expression[count+1].type == INTEGER and expression[count+2].type == INTEGER:
                        # if both integer
                        expression[count].value = str(self.evaluateExpression(errors,variables,expression[count:count+3]))
                    
                    elif (expression[count+1].type == VARIABLE and expression[count+2].type == INTEGER) or (expression[count+1].type == INTEGER and expression[count+2].type == VARIABLE) or (expression[count+1].type == VARIABLE and expression[count+2].type == VARIABLE):
                        check,index = -1,0

                        if self.checkAllVariables(expression[count+1],variables) == True:
                            check = 1
                            expression[count+1].value = self.retrieveFromVariables(expression[count+1],variables)
                        
                        if self.checkAllVariables(expression[count+2],variables) == True:
                            check = 1
                            expression[count+2].value = self.retrieveFromVariables(expression[count+2],variables)
                        
                        if check == 1:
                            expression[count].value = str(self.evaluateExpression(errors,variables,expression[count:count+3]))
                
                elif element.type == OPERATION and element.value == MEAN:
                    print("calculate for mean of all integer/variable/expression following")
                
                elif element.type == OPERATION and element.value == DISTANCE:
                    print("calculate for distance of all integer/variable/expression following")
                    
                count += 1
            
            del expression[start+1:end+1]
        
        if len(expression) == 3 and expression[0].type == OPERATION:
            output = -1
            operation,val1,val2 = expression[0].value,expression[1].value,expression[2].value

            if operation == PLUS:
                output = operations.add(int(val1),int(val2))
            elif operation == MINUS:
                output = operations.sub(int(val1),int(val2))
            elif operation == MULT:
                output = operations.mul(int(val1),int(val2)) 
            elif operation == DIV:
                output = operations.div(int(val1),int(val2)) 
            elif operation == MODU:
                output = operations.mod(int(val1),int(val2)) 
            elif operation == EXPO:
                output = adv_operations.exp(int(val1),int(val2))
            elif operation == ROOT:
                output = adv_operations.nthRoot(int(val1),int(val2))
            
            return output
        elif len(expression) == 1 and (expression[0].type == VARIABLE or expression[0].type == INTEGER or expression[0].type == STRING):
            # if variable
            if expression[0].type == STRING:
                return expression[0].value[1:len(expression[0].value)-1]
            else:  
                return expression[0].value
        else:
            errors += 1
            return errors

def main():
    block_end = False
    block_start = False
    code_block = []

    testIO = InputOutput()
    def_locn = "C:/Users/lenovo/Documents/GitHub/python-workspace/"

    test_source = testIO.inputSourceFile()
    check_source = testIO.checkIpolFile(test_source)

    source_code = []
    errors = 0
        
    if check_source != "INVALID SOURCE FILE!":
        print(def_locn+test_source)
        source_code = testIO.readIpolFile(def_locn+test_source)
        print(source_code)

    for statement in source_code:
        if statement == "CREATE" and block_start != True:
            # start reading in cobe block
            block_start = True
        elif statement == "RUPTURE" and block_start == True:
            if block_end != True: # first instance of rupture
                block_end = True
                #code_block.append(statement)
                break
            elif block_start == True: # has existing rupture
                errors += 1
        elif statement == "CREATE" and block_start == True:
            errors += 1
            break
        elif block_start == True and block_end != True:
            code_block.append(statement)
            
    # process code block
    if errors == 0:
        code_block = InterpolBody(code_block,False,False)
        code_block.processBlock()
    else:
        print("SYNTAX ERROR!")

main()