"""Jinja2 template rendering for email body."""
from jinja2 import Environment, FileSystemLoader
import os


def render_email(template_path: str, context: dict) -> tuple[str, str]:
    """Render the email template and return (subject, body)."""
    template_dir = os.path.dirname(os.path.abspath(template_path))
    template_file = os.path.basename(template_path)

    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_file)

    rendered = template.render(**context)
    subject = context.get("subject", "Hello from Email Automation")
    return subject, rendered
