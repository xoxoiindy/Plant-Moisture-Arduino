
from twilio.rest import Client
import serial
import time
import config

#Twilio API
account_sid = config.account_sid
auth_token = config.auth_token
client = Client(account_sid, auth_token)


def textTimer():
    time.sleep(3600)

def plantMonitor():                                                                                                                                                                                                                      ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1)                                                                                                                                                                   while True:                                                                                                                                                                                                                              ser.flush()
        while True:
            try:
                moisty = ser.readline().decode('utf-8').rstrip()
                moisty = int(moisty)
            except:
                continue
            break
        print("Moisture Level " + str(moisty))

        if moisty > 800:

            # Print message in the terminal for reference
            message = "Thirsty for H20..."
            # Txt notification
            txt_message = client.messages \
                .create(
                body=message,
                from_= config.tw_cell ,
                to= config.per_cell 
                )
            print(txt_message.sid)
            textTimer()

if __name__ == '__main__':
    plantMonitor()