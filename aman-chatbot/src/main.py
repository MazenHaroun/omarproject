# filepath: /aman-chatbot/aman-chatbot/src/main.py

from twilio_client import TwilioClient
from chatbot import ChatBot

def main():
    # Initialize Twilio client
    twilio_client = TwilioClient()
    
    # Initialize chatbot
    chatbot = ChatBot()

    # Send welcome message
    welcome_message = "مرحبًا بكم في أمان للأنظمة! كيف يمكنني مساعدتكم اليوم؟"
    twilio_client.send_message(welcome_message)

    # Start listening for user input (this is a placeholder for actual implementation)
    while True:
        user_input = twilio_client.receive_message()
        response = chatbot.get_response(user_input)
        twilio_client.send_message(response)

if __name__ == "__main__":
    main()