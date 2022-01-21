from random import choice
import requests as r
import time
from dotenv import dotenv_values

s = r.Session()

dict_id = {'1': 916028596286525500, '2': 931137672733401088, '3': 926458709285175406}
dict_files = {'1': 'newgemtext.txt', '2': 'rank.txt', '3': 'pioneer.txt'}

tkn = int(input('Which Token?(1 - First; 2 - Second; 0 - another): '))
if tkn == 0:
    s.headers['authorization'] = input('Token: ')
else:
    s.headers['authorization'] = dotenv_values()[str(tkn)]

cht = int(input('Which chat?(1 - New gem; 2 - Check rank(new gem); 3 - Pioneer Shop; 0 - Another): '))
if str(cht) in dict_id:
    chat_id = dict_id[str(cht)]
    file_name = dict_files[str(cht)]
    print("id = "+ str(chat_id))
    print("file = " + str(file_name))
else:
    chat_id = int(input('Chat id: '))
    file_name = 'EnMsg.txt'
    print(file_name)

msg_set: list = open(file_name, 'r', encoding='utf-8').read().splitlines()
delay = int(input('Delay in seconds: '))
total_sent = count_errors = 0
plus_second = int(input('Do you want to add a second to delay for avoiding errors?(1 - Yes; 0 - No): '))
if plus_second:
    delay += 1

i = int(0)
maxim = sum(1 for line in open(file_name,'r', encoding='utf-8'))

while True:
    try:
        if i >= maxim - 1:
            i = 0
        msg = msg_set[i]
        _data = {'content': msg, 'tts': False}
        resp = s.post(
            f'https://discord.com/api/v9/channels/{chat_id}/messages', json=_data).json()
        msg_id = resp['id']
        total_sent += 1
        print(f'{total_sent}) Sent: {msg}')
        print(f'Delay: {delay} seconds')
        time.sleep(delay)
        i += 1
    except Exception as e:
        count_errors += 1
        print(f'Error ' + str(count_errors) + ') ' f'{e}')
        time.sleep(5)
