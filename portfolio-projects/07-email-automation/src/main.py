"""Entry point for the Email Automation Tool."""
import argparse
from contacts import load_contacts
from template import render_email
from mailer import send_email, log_result


def main():
    parser = argparse.ArgumentParser(description="Email Automation Tool")
    parser.add_argument("--contacts", default="contacts/contacts.csv", help="Path to contacts CSV")
    parser.add_argument("--template", default="templates/email_body.html", help="Path to email template")
    parser.add_argument("--dry-run", action="store_true", help="Preview emails without sending")
    args = parser.parse_args()

    contacts = load_contacts(args.contacts)
    print(f"Loaded {len(contacts)} contacts.")

    for contact in contacts:
        subject, body = render_email(args.template, contact)
        if args.dry_run:
            print(f"\n--- DRY RUN: {contact['email']} ---")
            print(f"Subject: {subject}\n{body}")
        else:
            success, message = send_email(contact["email"], subject, body)
            log_result(contact["email"], success, message)
            status = "sent" if success else f"failed: {message}"
            print(f"{contact['email']}: {status}")


if __name__ == "__main__":
    main()
