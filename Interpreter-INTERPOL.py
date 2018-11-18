DINT,DST,STORE,PRINT,PRINTN = "DINT","DSTR","STORE","GIVEYOU!","GIVEYOU!!"
DECLARATION_INT,DECLARATION_STR = "DECLARATION_INTEGER","DECLARATION_STRING"
PLUS,MINUS,MULT,DIV,MODU = "PLUS","MINUS","MULT","DIV","MODU"
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

    def inputFromUser(self):
        # Asking input from the user:  GIVEME? <variable_name>
        return input("GIVEME? ")    

    def printOutput(self,tag,output_block):
        if tag == 1:
            # Printing values, variables, and expressions: GIVEYOU! <expression>
            return print("GIVEYOU!",output_block)
        elif tag == 2:
            # Printing values, variables, and expressions with a new line affixed at the end: GIVEYOU!! <expression>
            return print("GIVEYOU!!",output_block,"\n")

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
        
        if(len(ipol_file.split(".")) <= 1 or ipol_file.split(".")[1] != "ipol"):
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
        return expr

    def avg(self,values):
        # Average: MEAN <expr1> <expr2> <expr3> … <exprn>
        #  This is the only operation that accepts an unlimited number of parameters.
        return values

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
            temp_symb_table,syntax_errors = self.checkSyntax(temp_tokens)
            all_symb_table.append(temp_symb_table)
            
            for each_token in temp_symb_table:
                print(each_token.type,each_token.value)
             
            grammar_errors,variables = self.checkGrammar(temp_symb_table)
            for var in variables:
                if len(variables) != 0:
                    all_variables.append(var)
                    
            print(all_variables)
            #print(syntax_errors,grammar_errors)

            #if syntax_errors > 0 or grammar_errors > 0:
            #    print("SYNTAX ERROR!")
            #    break
            #else:
            #    i+=1
    
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

            elif block_line[i].find("[") != -1:
                
                token_type = STRING
                self.syntax_status = True
            
            elif block_line[i] == PRINT:
                token_type = PRINT
               # self.syntax_status = True
            
            elif block_line[i] == PRINTN:
                token_type = PRINTN
                #self.syntax_status = True
            
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


    def checkGrammar(self,block_line):

        # check grammar of code block
        # code block is broken down into symbol table
        # check if arrangement of tokens are valid

        isDeclaration = 0
        isAssignment = 0
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

            print(token)

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
                    eval_result = self.evaluateExpression(errors,variables,temp_expression)
                    print(eval_result)
                    temp_expression =[]

            elif token.type == VARIABLE_ASSIGNMENT:
                # check if "IN"
                # should be assignment (store) and expression before
                if isAssignment == 1 and isDeclaration == 0:
                    expression_end = token_count
                    hasIn = 1
                    expressions.append(temp_expression)
                    #evaluate expression
                    eval_result = self.evaluateExpression(errors,variables,temp_expression)
                    print(eval_result)
                    temp_expression =[]

            elif token.type == PRINT and token_count == 0:
                # print value of following variable
                isPrint = 1
                
            elif token.type == PRINTN and token_count == 0:
                    # print value of following variable with newline
                isPrint = 1
            
            elif isDeclaration == 1 and isPrint == 0 and isAssignment == 0 and token.type != DECLARATION_ASSIGNMENT and token.type != VARIABLE_ASSIGNMENT:
                #should read in an expression
                #if expression_end != 1 and expression_start == 1:
                if token.type == VARIABLE and declarationType == "int":
                    variables.append([INTEGER,token.value,-1])
                elif token.type == VARIABLE and declarationType == "string":
                    variables.append([STRING,token.value,"-"])

                temp_expression.append(token)
            elif isAssignment == 1 and isPrint == 0 and isDeclaration == 0 and token.type != VARIABLE_ASSIGNMENT and token.type != DECLARATION_ASSIGNMENT:
                #should read in an expression
                #if expression_end != 1 and expression_start == 1:
                print(eval_result)
                #check in list of all variables if existing
                if token.type == VARIABLE:
                    variables.append([STRING,token.value,eval_result])
                
                temp_expression.append(token)
            elif isPrint == 1 and isDeclaration == 0 and isAssignment == 0 and token.type != DECLARATION_ASSIGNMENT and token.type != VARIABLE_ASSIGNMENT:
                #should read in an expression
                #if expression_end != 1 and expression_start == 1:
                if token.type == VARIABLE and declarationType == "int":
                    variables.append([INTEGER,token.value,-1])
                elif token.type == VARIABLE and declarationType == "string":
                    variables.append([STRING,token.value,"-"])

                temp_expression.append(token)
            else:
                errors += 1

            print(token_count,errors,token)
            token_count += 1
        expressions.append(temp_expression)
        eval_result = self.evaluateExpression(errors,variables,temp_expression)
        print(eval_result)

        if isDeclaration == 1 and isPrint == 0 and isAssignment == 0 and token.type != DECLARATION_ASSIGNMENT and token.type != VARIABLE_ASSIGNMENT and hasWith == 1:
            # works for code blocks with only 1 variable
            variables[0][2] = eval_result

        print("expressions",expressions)
        print("variables",variables)
        
        return errors, variables

    def evaluateExpression(self,errors,variables,expression):
        operations = ArithmeticOperations([])
        print("ineval",expression)
        
        while len(expression) > 3:
        
            count,start,end = 0,0,0
            
            for element in expression:
                if element.type == OPERATION: # if operation
                    start,end = count,count+2
                    if expression[count+1].type == INTEGER and expression[count+2].type == INTEGER:
                        # if both integer
                        expression[count].value = str(self.evaluateExpression(errors,variables,expression[count:count+3]))
                    
                    elif (expression[count+1].type == VARIABLE and expression[count+2].type == INTEGER) or (expression[count+1].type == INTEGER and expression[count+2].type == VARIABLE) or (expression[count+1].type == VARIABLE and expression[count+2].type == VARIABLE):
                        print("hi", variables)
                        check,index = -1,0
                        
                        for variable in variables:
                            if variable[1] == expression[count+1].value:
                                check = 1
                                expression[count+1].value = variable[2]
                            if  variable[1] == expression[count+2].value:
                                check = 1
                                expression[count+2].value = variable[2]

                        if check == 1:
                            print("change", expression,expression[count:count+3])
                            expression[count].value = str(self.evaluateExpression(errors,variables,expression[count:count+3]))
                count += 1
            
            del expression[start+1:end+1]
            print(expression)
        
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
                
            return output
        elif len(expression) == 1 and (expression[0].type == VARIABLE or expression[0].type == INTEGER or expression[0].type == STRING):
            # if variable
            return expression[0].value
        else:
            errors += 1
            return errors

def main():
    # TEST FOR INTERPRETER. NOT ACTUAL INPUT METHOD
    block_end = False
    block_start = False
    code_block = []

    testIO = InputOutput()
    def_locn = "C:/Users/lenovo/Documents/GitHub/python-workspace/"

    test_source = testIO.inputFromUser()
    check_source = testIO.checkIpolFile(test_source)

    source_code = []

    print(check_source)
        
    if check_source != "INVALID SOURCE FILE!":
        print(def_locn+test_source)
        source_code = testIO.readIpolFile(def_locn+test_source)
        print(source_code)

    for statement in source_code:
        if statement == "CREATE":
            # start reading in cobe block
            block_start = True

        elif statement == "RUPTURE":
            block_end = True
            break
        
        elif block_start == True:
            code_block.append(statement)
            
    # process code block
    code_block = InterpolBody(code_block,False,False)
    code_block.processBlock()

main()