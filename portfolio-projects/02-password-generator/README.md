# Password Generator

A CLI tool that generates secure, customizable passwords based on user-defined rules.

## Portfolio Description

A secure password generator that produces cryptographically random passwords based on configurable rules — length, character sets, and complexity. Includes a password strength estimator and clipboard integration. Uses Python's `secrets` module rather than `random` to ensure cryptographic safety.

## Features

- Configurable length and character sets (uppercase, lowercase, digits, symbols)
- Generate multiple passwords at once
- Password strength indicator (weak / medium / strong)
- Copy to clipboard

## Tech Stack

- Python 3
- `secrets`, `string`, `argparse`, `pyperclip`

## Project Structure

```
02-password-generator/
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── main.py             # entry point, CLI interface
│   ├── generator.py        # password generation logic
│   └── strength.py         # strength estimation logic
└── tests/
    └── test_generator.py
```

## Getting Started

```bash
pip install -r requirements.txt
python src/main.py
```

## Usage

```bash
# Interactive mode
python src/main.py

# With arguments
python src/main.py --length 16 --count 3 --no-symbols
```

## Status

🚧 In progress
