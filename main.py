""" 1. twilio client setup
2. user inputs
3. seheduling logic
4. sent message
"""

from twilio.rest import Client
from datetime import datetime,timedelta
import time


account_sid=''
auth_token=''
client=Client(account_sid,auth_token)

def sent_mess(recipient_number,message_body):
    try:
        message=Client.messages.create(
            from_='whatsapp: ',
            body=message_body,
            to=f'whatsapp{recipient_number}'

        )
        print(f'Message send successfully{message.sid}')
    except Exception as e:
        print("an error occured")

name=input("enter the receipent number: ")
recipient_num=input("enter receipent number with country code: ")
message_body=input(f"enter message you want to sent :{name} ")
date_str=input("enter the date to sent message(YYYY-MM-DD): ")
time_str=input("enter the time to sent message (HH:MM in 24 hours format)")
schedule_datatime = datetime.strptime(f'{date_str}{time_str}', "%Y-%m-%d %H%M")



current_datetime=datetime.now()
time_differnce=schedule_datatime-current_datetime
delay_second=time_differnce.total_seconds()


if delay_second<=0:
    print("the specified time and date is in past .. please enter the future date and time")
else:
    print(f"Message scheduled to be send to {name} at {schedule_datatime}")


    time.sleep(delay_second)

sent_mess(recipient_num,message_body)

