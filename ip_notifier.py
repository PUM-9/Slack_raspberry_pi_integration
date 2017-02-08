import netifaces as ni
import requests
from config import WEBHOOK, INTERFACE
import time


def get_ip():
    try:
        ip = ni.ifaddresses(INTERFACE)[ni.AF_INET][0]['addr']
    except KeyError:
        ip = None
    return ip

if __name__ == "__main__":
    tries = 0
    ip = get_ip()
    while not ip and tries < 15:
        time.sleep(60)
        ip = get_ip()
        tries += 1
    payload = {'text': ip, 'username': 'pi-bot', 'icon_emoji': ':robot_face:'}
    requests.post(WEBHOOK, json=payload)
