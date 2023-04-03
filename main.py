import os
from mail import send_email
from dotenv import load_dotenv

load_dotenv()
PASSWORD = os.environ.get('PASSWORD')
EMAIL = os.environ.get('EMAIL')

def main(MESSAGE):
    
    send_email(EMAIL,MESSAGE,PASSWORD)
    print('Email sent!')

MESSAGE = "Hey there! This is a dummy text!"

main(MESSAGE)
