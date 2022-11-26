from twilio.rest import Client


class NotificationManager:
    TWILIO_SID = "ACd49222ff0c291f1996451b3dd003c6e3"
    TWILIO_AUTH_TOKEN = "1571b1c48625d6ecfadfe9c3d759cf59"
    TWILIO_VIRTUAL_NUMBER = "##########"
    TWILIO_VERIFIED_NUMBER = "#########"

    def __init__(self):
        self.client = Client(self.TWILIO_SID, self.TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages \
            .create(
            body=message,
            from_=self.TWILIO_VIRTUAL_NUMBER,
            to=self.TWILIO_VERIFIED_NUMBER
        )
