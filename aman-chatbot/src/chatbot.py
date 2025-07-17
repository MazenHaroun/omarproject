from .responses import welcome_message, main_sections, get_response

class ChatBot:
    def __init__(self):
        self.started = False

    def handle_message(self, user_input):
        if not self.started:
            self.started = True
            return f"{welcome_message}\n{main_sections}"
        else:
            return get_response(user_input)