class TwilioClient:
    def __init__(self, account_sid, auth_token, from_number):
        from twilio.rest import Client
        self.client = Client(account_sid, auth_token)
        self.from_number = from_number

    def send_message(self, to_number, message):
        message = self.client.messages.create(
            body=message,
            from_=self.from_number,
            to=to_number
        )
        return message.sid

    def receive_messages(self):
        # This method can be implemented to handle incoming messages
        pass