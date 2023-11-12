import getpass
import requests
import time

def get_discord_token():
    try:
        discord_token = getpass.getpass("Input Discord token: ")
        response = requests.get('https://discord.com/api/v9/users/@me/library', headers={"Authorization": discord_token})
        response.raise_for_status()
        return discord_token
    except Exception:
        print("Invalid discord token!")
        return get_discord_token()

def get_channel_id():
    try:
        channel_id = int(input("Input channel id: "))
        current_epoch = int(time.time())
        if channel_id < 1420070400 and channel_id <= current_epoch:
            raise Exception("Invalid Channel ID! Snowflakes can't be less than discord epoch or in the future!")
    except Exception as err:
        print(err)
        return get_channel_id()

def get_total_executions():
    try:
        return int(input("Input the total number of planned executions: "))
    except Exception:
        return get_total_executions()
