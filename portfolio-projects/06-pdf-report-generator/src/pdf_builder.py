"""Build the PDF report using fpdf2."""
from fpdf import FPDF
from datetime import datetime


class ReportPDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 14)
        self.cell(0, 10, "Expense Report", align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font("Helvetica", "", 9)
        self.cell(0, 6, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")


def build_report(data: list[dict], chart_path: str, output_path: str):
    pdf = ReportPDF()
    pdf.add_page()

    # Summary table
    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(0, 8, "Transaction Summary", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 9)

    totals = {}
    for row in data:
        totals[row["category"]] = totals.get(row["category"], 0) + row["amount"]

    col_w = [80, 40]
    pdf.set_fill_color(200, 220, 255)
    pdf.cell(col_w[0], 7, "Category", border=1, fill=True)
    pdf.cell(col_w[1], 7, "Total ($)", border=1, fill=True, new_x="LMARGIN", new_y="NEXT")

    for cat, total in sorted(totals.items()):
        pdf.cell(col_w[0], 7, cat, border=1)
        pdf.cell(col_w[1], 7, f"{total:.2f}", border=1, new_x="LMARGIN", new_y="NEXT")

    grand_total = sum(totals.values())
    pdf.set_font("Helvetica", "B", 9)
    pdf.cell(col_w[0], 7, "TOTAL", border=1)
    pdf.cell(col_w[1], 7, f"{grand_total:.2f}", border=1, new_x="LMARGIN", new_y="NEXT")

    # Chart
    pdf.ln(6)
    pdf.image(chart_path, w=180)

    pdf.output(output_path)
