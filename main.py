import requests
import time
from config import TELEGRAM_TOKEN, CHANNEL_ID , USERS

status = ['offline' for each in USERS ]
TIME = [0 for each in USERS ]

def send_message(message):
    url = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=markdown".format(TELEGRAM_TOKEN, CHANNEL_ID, message) 
    res = requests.get(url)

def get_status():
    for ind, each in enumerate(USERS):
        res = requests.get("https://services.chess.com/service/presence/users?ids="+each[0])
        st = res.json()['users'][0]['status'];print(st)
        if(st == 'offline'):
            if(TIME[ind] != 0):
                send_message(each[1] + "  went offline after being online for "+str(TIME[ind]) + " minute(s)")
                TIME[ind] = 0
        elif(st == 'online'):
            if(TIME[ind] == 0):
                send_message(each[1] + " just came online")
                TIME[ind] += 0.5
            else:
                TIME[ind]  += 0.5



def main():
    print("starting....");send_message("STARTED APPLICATION")
    while True:
        get_status()
        time.sleep(30)


if __name__ == "__main__":
    main()
