import pandas as pd
import smtplib
import logging


def send_email(sender_email,text, sender_pwd):

    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='email_process.log')

    try:
        df = pd.read_csv("mail.csv")
    except FileNotFoundError:
        print('File not found!')
        logging.critical('File not found')
    except:
        print(' An error occured while reading the file.')
    column_name = 'email'
    col = df[column_name]
    receiver_email =col.values.tolist()
    logging.info('Read the file')

    for emailId in receiver_email:
        print(emailId)

    
        message = text
        logging.info('sending of email processed')


        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout= 10) as smtp:
                smtp.login(sender_email, sender_pwd)
                smtp.sendmail(sender_email, emailId , message)
        except Exception as e:
            print(f'An error occured while sending email. Please try again: {str(e)}')
            logging.critical(f'An error occured while sending email. Please try again: {str(e)}')



