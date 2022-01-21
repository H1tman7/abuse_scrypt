from random import choice
import requests as r
import time

s = r.Session()
s.headers['authorization'] = input('Token: ')
msg_set: list = open('msg.txt', 'r', encoding='utf-8').read().splitlines()
chat_id = input('Input chat id: ')
delay = int(input('Delay between messages in seconds: '))
total_sent = 0


while True:
    try:
        msg = choice(msg_set)
        print(f'Sending message {msg}')
        _data = {'content': msg, 'tts': False}
        resp = s.post(
            f'https://discord.com/api/v9/channels/{chat_id}/messages', json=_data).json()
        msg_id = resp['id']
        total_sent += 1
        print(f'Message sent (Already {total_sent} in total).')
        print(f'Sleeping {delay} seconds')
        time.sleep(delay)
    except Exception as e:
        print(f'Some error: {e}')
        time.sleep(20)