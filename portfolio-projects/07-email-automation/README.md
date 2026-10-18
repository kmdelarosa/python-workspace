# Email Automation Tool

A mail-merge style tool that reads a CSV of contacts and sends personalized emails via SMTP.

## Portfolio Description

A mail-merge automation tool that generates and sends personalized emails from a CSV contact list and a reusable template. Supports HTML emails, a dry-run preview mode, and per-contact send logging. SMTP credentials are managed via environment variables. Built to demonstrate automation, templating, and responsible handling of sensitive config.

## Features

- CSV input with name, email, and custom merge fields
- Jinja2 template engine for email body
- HTML and plain text email support
- Dry-run mode: render and preview without sending
- Per-contact send log (success / failure)
- SMTP credentials via `.env` file

## Tech Stack

- Python 3
- `smtplib`, `email`, `csv`
- `python-dotenv`, `jinja2`

## Project Structure

```
07-email-automation/
├── README.md
├── requirements.txt
├── .env.example            # template for SMTP credentials
├── contacts/
│   └── contacts.csv        # example contacts file
├── templates/
│   ├── email_body.html     # HTML email template
│   └── email_body.txt      # plain text fallback
├── logs/
│   └── send_log.csv        # per-contact send results
├── src/
│   ├── __init__.py
│   ├── main.py             # entry point, CLI args
│   ├── mailer.py           # SMTP send logic
│   ├── template.py         # Jinja2 template rendering
│   └── contacts.py         # CSV contact loading
└── tests/
    └── test_template.py
```

## Getting Started

```bash
pip install -r requirements.txt

# Copy and fill in your SMTP credentials
cp .env.example .env

# Dry run first
python src/main.py --dry-run

# Send emails
python src/main.py
```

## Environment Variables

```
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your@email.com
SMTP_PASS=your_app_password
EMAIL_FROM=Your Name <your@email.com>
```

## Status

🚧 In progress
