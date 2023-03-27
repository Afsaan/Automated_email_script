import pandas as pd
import smtplib
import os 
from dotenv import load_dotenv
import re

#def dest_email():
    

    # for emailId in receiver_email:
    #     print(emailId)
    # while True:
    #     if not re.match(r"[^@]+@[^@]+\.[^@]+", receiver_email):
    #         print('Invalid email address. Please try again.')
    #     else:
    #         print('Your email is being sent to:', receiver_email)

    #     return receiver_email

def send_email(sender_email,text, sender_pwd):
    sender_email = sender_email

    df = pd.read_csv("mail.csv")
    col = df.iloc[:, 2] #make it dynamic 
    receiver_email =col.values.tolist()
    print(receiver_email)

    for emailId in receiver_email:
        print(emailId)
        message = ("%s", text)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_pwd)
            smtp.sendmail(sender_email, emailId , message,)

def main():
    load_dotenv()
    sender_pwd = os.environ.get('PASSWORD')
    send_email('harishpanjikar@gmail.com','wallah','ulsolqvvokxgdmiv')
    print('Email sent!')


if __name__ == '__main__':
    main()







"""
env varibale create - env varibale
create functional
"""

