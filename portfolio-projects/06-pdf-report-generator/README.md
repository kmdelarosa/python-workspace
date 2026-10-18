# PDF Report Generator

A CLI tool that reads structured CSV data and generates a formatted PDF report.

## Portfolio Description

A CLI tool that reads structured CSV data and generates a formatted PDF report — including summary tables, category breakdowns, and a bar chart. Accepts input/output paths as arguments and handles malformed data gracefully. Demonstrates data processing, programmatic document generation, and clean CLI design.

## Features

- Read data from a CSV file
- Generate PDF with: title page, summary table, category breakdown, bar chart
- Configurable template (colors, fonts, logo placeholder)
- CLI interface with `--input` and `--output` flags
- Graceful handling of missing or malformed data

## Tech Stack

- Python 3
- `csv`, `argparse`
- `fpdf2`
- `matplotlib` (chart generation)

## Project Structure

```
06-pdf-report-generator/
├── README.md
├── requirements.txt
├── sample_data/
│   └── expenses.csv        # example input file
├── output/                 # generated PDFs saved here
├── src/
│   ├── __init__.py
│   ├── main.py             # entry point, CLI args
│   ├── reader.py           # CSV parsing and validation
│   ├── charts.py           # matplotlib chart generation
│   └── pdf_builder.py      # fpdf2 PDF assembly
└── tests/
    └── test_reader.py
```

## Getting Started

```bash
pip install -r requirements.txt
python src/main.py --input sample_data/expenses.csv --output output/report.pdf
```

## Status

🚧 In progress
