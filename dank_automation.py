import requests
import time
from dank_analysis import display_time_info

def perform_dank_action(action, i):
    payload = {"content": f"pls {action}"}
    requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers={"authorization": discord_token})
    return i+1

def automate_coin_collection(repeat_count, action_list):
    for i in range(repeat_count):
        for action in action_list:
            completed_executions = perform_dank_action(action, i)
        print("Set of dank actions performed: {completed_executions}")
        display_time_info(total_executions, completed_executions)
        time.sleep(35)

# Replace "Token here" with your actual Discord token
discord_token = "Token here"
channel_id = int(input("Input Discord channel ID: "))

# Call the function to display estimated time
total_executions = int(input("Input the total number of planned executions: "))
actions_list = ['fish', 'hunt', 'dig', 'beg']

automate_coin_collection(total_executions, actions_list)
