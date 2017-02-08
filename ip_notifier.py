import netifaces as ni
import requests
from config import WEBHOOK, INTERFACE

if __name__ == "__main__":
    try:
        ip = ni.ifaddresses(INTERFACE)[ni.AF_INET][0]['addr']
    except KeyError:
        ip = "Saknar wifi"
    payload = {'text': ip, 'username': 'pi-bot', 'icon_emoji': ':robot_face:'}
    requests.post(WEBHOOK, json=payload)
