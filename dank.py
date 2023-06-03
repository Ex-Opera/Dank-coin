import requests
import time

channelID = int(input("Input channel_ID: "))
headers = {"authorization": "Token here"}

def dank(action):
  payload = {'content': f'pls {action}'}
  requests.post(f'https://discord.com/api/v9/channels/{channelID}/messages', data=payload, headers=headers)
  print(f'{action} {i+1}')

repeat = int(input("Input number of repeat: "))
actions = ['fish', 'hunt', 'dig', 'beg']

for i in range(repeat):
  for action in actions:
    dank(action)
  time.sleep(35)
