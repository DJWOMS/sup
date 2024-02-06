import smtplib
import ssl
from email.mime.text import MIMEText

from dotenv import load_dotenv
import os

load_dotenv()


class EmailService:
    """Basic Service to send emails"""
    def __init__(self):
        # Credentials

        self.user: str = os.getenv("EMAIL_USER")
        self.password: str = os.environ.get('EMAIL_PASSWORD')

        # Server config
        self.smtp_port = 465
        self.smtp_server = "smtp.gmail.com"
        self.smtp_context = ssl.create_default_context()

    def send_email(self, recipient_email: str, subject: str, body: str) -> None:

        # Message config
        message = MIMEText(body)
        message["Subject"] = subject
        message["From"] = self.user
        message['To'] = recipient_email

        # Message sending
        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, context=self.smtp_context) as smtp:
            smtp.login(self.user, self.password)
            smtp.sendmail(self.user, recipient_email, message.as_string())


