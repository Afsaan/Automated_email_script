import pandas as pd
import smtplib
import logging
from constant import FILE_PATH,SERVER_URL,PORT

def send_email(sender_email,text, sender_pwd):

    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='email_process.log')
    
    FILE_PATH = input("enter file name or path:")

    try:
        df = pd.read_csv(FILE_PATH)
        column_name = 'email'
        col = df[column_name]
        receiver_email =col.values.tolist()
    except FileNotFoundError:
        logging.critical('File not found')
        data = input("enter the emails you want the data to send to:")
        receiver_email = data.split(',')
    except:
        logging.critical(' An error occured while reading the file.')
    
    logging.info('Read the file')

    for emailId in receiver_email:
        print(emailId)

    
        message = text
        logging.info('sending of email processed')


        try:
            with smtplib.SMTP_SSL(SERVER_URL, PORT, timeout= 10) as smtp:
                smtp.login(sender_email, sender_pwd)
                smtp.sendmail(sender_email, emailId , message)
        except Exception as e:
            logging.critical(f'An error occured while sending email. Please try again: {str(e)}{emailId}')



