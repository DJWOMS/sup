import aiosmtplib
from email.mime.text import MIMEText
from src.app.config.email_config import settings


class EmailService:
    """Basic Service to send emails"""
    def __init__(self):
        # Credentials

        self.user = settings.email_username
        self.password = settings.email_password

        # Server config
        self.smtp_port = settings.smtp_port
        self.smtp_host = settings.smtp_host

    async def send_email(self, recipient_email: str, subject: str, body: str) -> None:

        # Message config
        message = MIMEText(body)
        message["Subject"] = subject
        message["From"] = self.user
        message['To'] = recipient_email

        # Email sending
        await aiosmtplib.send(
            message.as_string(),
            sender=self.user,
            recipients=recipient_email,
            hostname=self.smtp_host,
            port=self.smtp_port,
            username=self.user,
            password=self.password,

        )


