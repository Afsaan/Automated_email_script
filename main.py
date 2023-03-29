import pandas as pd
import smtplib
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='order_processing.log')



def send_email(sender_email,text, sender_pwd):

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

        try:
            message = text
        except ValueError:
            print('The body of the email is empty.')
            logging.info('The message is empty')
        finally:
            print('sending an empty email')
            logging.info('sending of email processed')


        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout= 10) as smtp:
                smtp.login(sender_email, sender_pwd)
                smtp.sendmail(sender_email, emailId , message)
        except Exception as e:
            print(f'An error occured while sending email. Please try again: {str(e)}')
            logging.critical(f'An error occured while sending email. Please try again: {str(e)}')

def main():
    send_email('harishpanjikar@gmail.com','wallah','ulsolqvvokxgdmiv')
    print('Email sent!')


if __name__ == '__main__':
    main()



