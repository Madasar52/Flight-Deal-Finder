from twilio import Client
import os

acc_sid = os.environ.get("acc_sid")
auth_token = os.environ.get("auth_token")

class NotificationManager:
    def __init__(self):
        self.client = Client(acc_sid, auth_token)

    def send_sms(self, message):
        message = self.client.messages\
            .create(
            body= message,
            from_= '+12056724168',
            to= '+16475744548',
        )
        print(message.sid)
