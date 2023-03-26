import pandas as pd
import smtplib
import os 
from dotenv import load_dotenv
import re

def dest_email():
    while True:
        receiver_email = input("Please enter the receiver's address:")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", receiver_email):
            print('Invalid email address. Please try again.')
        else:
            print('Your email is being sent to:', receiver_email)

        return receiver_email

def send_email():
    sender_email = 'harishpanjikar@gmail.com'
    sender_pwd = os.environ.get('PASSWORD')
    receiver_email = dest_email()

    message = "Hey nothing serious. Just testing!"

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, sender_pwd)
        smtp.sendmail(sender_email, receiver_email, message)

def main():
    load_dotenv()
    send_email()
    print('Email sent!')


if __name__ == '__main__':
    main()



# df = pd.read_csv("mail.csv")
# col = df.iloc[:, 2]
# d_list =col.values.tolist()
# print(d_list)






"""
env varibale create - env varibale
create functional
"""

