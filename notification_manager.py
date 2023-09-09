from twilio.rest import Client
import os

class NotificationManager:
    def __init__(self):
        self.account_sid = os.environ.get("TWILIO_ACCOUNT_ID")
        self.auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
        self.client = Client(self.account_sid, self.auth_token)

    def send_message(self, text):
        message = self.client.messages.create(
            from_="+12184323850",
            body=text,
            to="+5541996039357"
        )
