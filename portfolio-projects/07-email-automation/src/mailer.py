"""SMTP email sending and send logging."""
import csv
import os
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASS = os.getenv("SMTP_PASS", "")
EMAIL_FROM = os.getenv("EMAIL_FROM", SMTP_USER)

LOG_PATH = os.path.join(os.path.dirname(__file__), "..", "logs", "send_log.csv")


def send_email(to: str, subject: str, html_body: str) -> tuple[bool, str]:
    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = EMAIL_FROM
        msg["To"] = to
        msg.attach(MIMEText(html_body, "html"))

        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.sendmail(EMAIL_FROM, to, msg.as_string())

        return True, "ok"
    except Exception as e:
        return False, str(e)


def log_result(email: str, success: bool, message: str):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    write_header = not os.path.exists(LOG_PATH)
    with open(LOG_PATH, "a", newline="") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["timestamp", "email", "status", "message"])
        writer.writerow([datetime.now().isoformat(), email, "sent" if success else "failed", message])
