import netifaces as ni
import requests

WEBHOOK = "https://hooks.slack.com/services/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"

if __name__ == "__main__":
    try:
        ip = ni.ifaddresses('wlp2s0')[ni.AF_INET][0]['addr']
    except KeyError:
        ip = "Saknar wifi"
    payload = {'text': ip, 'username': 'pi-bot', 'icon_emoji': ':robot_face:'}
    requests.post(WEBHOOK, json=payload)
