

class NotificationService:

    async def email_confirmation(self, user_verify: str):
        print(f"https://127.0.0.1:8000/verify/{user_verify}")
