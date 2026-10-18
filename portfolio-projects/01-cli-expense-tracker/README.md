# CLI Expense Tracker

A command-line app to log, view, and summarize personal expenses stored in a CSV file.

## Portfolio Description

A command-line expense tracker built in Python that lets you log, categorize, and summarize your spending. Data is persisted to a CSV file between sessions, with filtering by category and date range. Built to practice core Python fundamentals — data structures, file I/O, and input validation.

## Features

- Add expenses with date, category, amount, and description
- View all expenses or filter by category / date range
- Summary report: totals by category and by month
- Delete an expense by ID
- Input validation and error handling throughout

## Tech Stack

- Python 3
- `csv`, `os`, `datetime`, `argparse`

## Project Structure

```
01-cli-expense-tracker/
├── README.md
├── requirements.txt
├── data/
│   └── expenses.csv        # auto-created on first run
├── src/
│   ├── __init__.py
│   ├── main.py             # entry point, CLI menu
│   ├── tracker.py          # add / delete / list logic
│   └── reports.py          # summary and filtering logic
└── tests/
    └── test_tracker.py
```

## Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python src/main.py
```

## Usage

```
Options:
  add       Add a new expense
  list      List expenses (optional: --category --from --to)
  summary   Show spending summary
  delete    Delete an expense by ID
  quit      Exit
```

## Status

🚧 In progress
