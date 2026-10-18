# Personal Finance Dashboard

An OOP-based finance manager that evolves from a CLI tool into a Flask web dashboard.

## Portfolio Description

A personal finance management tool built with object-oriented Python. Tracks income and expenses across categories, compares spending against monthly budgets, and generates summary reports. Designed with a clean class architecture, this project demonstrates OOP principles, data modeling, and file persistence — with a web dashboard layer added using Flask.

## Features

- Add, edit, and delete transactions
- Set monthly budgets per category
- Spending vs. budget reports
- Export reports to PDF or CSV
- Phase 2: Flask web UI with charts

## Tech Stack

- Python 3
- `json`, `datetime`, OOP
- `fpdf2`, `matplotlib`
- `Flask` (phase 2)

## Project Structure

```
03-personal-finance-dashboard/
├── README.md
├── requirements.txt
├── data/
│   └── finance.json        # auto-created on first run
├── src/
│   ├── __init__.py
│   ├── main.py             # CLI entry point
│   ├── models/
│   │   ├── __init__.py
│   │   ├── transaction.py  # Transaction class
│   │   ├── category.py     # Category class
│   │   └── budget.py       # Budget class
│   ├── storage.py          # JSON read/write
│   ├── reports.py          # report generation
│   └── web/                # Phase 2 - Flask app
│       ├── __init__.py
│       └── app.py
└── tests/
    └── test_models.py
```

## Getting Started

```bash
pip install -r requirements.txt
python src/main.py
```

## Status

🚧 In progress — Phase 1 (CLI)
