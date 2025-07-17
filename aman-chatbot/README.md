# aman-chatbot

## Overview
"أمان للأنظمة" chatbot is a Python-based application that connects to Twilio to provide automated responses to user inquiries. The chatbot sends a welcome message upon starting and responds to user inputs based on predefined conditions.

## Project Structure
```
aman-chatbot
├── src
│   ├── main.py          # Entry point of the chatbot application
│   ├── chatbot.py       # Main logic of the chatbot
│   ├── twilio_client.py # Manages Twilio API connection
│   └── responses.py     # Contains predefined responses
├── requirements.txt     # Lists project dependencies
└── README.md            # Documentation for the project
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd aman-chatbot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Twilio account and obtain your Account SID and Auth Token.

4. Update the `twilio_client.py` file with your Twilio credentials.

## Usage
To start the chatbot, run the following command:
```
python src/main.py
```
The chatbot will send a welcome message and await user input.

## Functionality
- Sends a welcome message to users.
- Responds to user inquiries based on predefined conditions using if-else statements.
- Utilizes Twilio for sending and receiving messages.

## Contributing
Feel free to submit issues or pull requests for improvements or bug fixes.