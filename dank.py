import requests
import time
channelID = int(input("Input channel_ID: "))
headers = {"authorization": "Token here"}
def dank():
  requests.post(f'https://discord.com/api/v9/channels/{channelID}/messages', data = payload, headers = headers)
  if payload == {'content': 'pls fish'}: print(f'fish {i+1}')
  elif payload == {'content': 'pls hunt'}: print(f'hunt {i+1}')
  elif payload == {'content': 'pls dig'}: print(f'dig {i+1}')
  elif payload == {'content': 'pls beg'}: print(f'beg {i+1}')
repeat = int(input("Input number of repeat: "))
for i in range(repeat):
   payload = {'content': 'pls fish'}; dank()
   payload = {'content': 'pls hunt'}; dank()
   payload = {'content': 'pls dig'}; dank()
   payload = {'content': 'pls beg'}; dank()
   time.sleep(35)
