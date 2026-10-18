"""Entry point for the PDF Report Generator."""
import argparse
from reader import load_csv
from charts import generate_chart
from pdf_builder import build_report


def main():
    parser = argparse.ArgumentParser(description="PDF Report Generator")
    parser.add_argument("--input", required=True, help="Path to input CSV file")
    parser.add_argument("--output", required=True, help="Path for output PDF file")
    args = parser.parse_args()

    print(f"Reading data from {args.input}...")
    data = load_csv(args.input)

    print("Generating chart...")
    chart_path = generate_chart(data)

    print("Building PDF...")
    build_report(data, chart_path, args.output)

    print(f"Report saved to {args.output}")


if __name__ == "__main__":
    main()
