import pandas as pd
import smtplib


# df = pd.read_csv("mail.csv")
# col = df.iloc[:, 2]
# d_list =col.values.tolist()
# print(d_list)

sender_email = 'harishpanjikar@gmail.com'
receiver_email = 'harishpanjikar.work@gmail.com'


message = "Hey nothing serious. Just testing!"

# def send_email(text):
#     return "Hey nothing serious. Just testing!"

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(sender_email, sender_pwd)
    smtp.sendmail(sender_email, receiver_email, message)


"""
env varibale create - env varibale
create functional
"""

