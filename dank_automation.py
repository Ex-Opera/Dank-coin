import requests
import time
from dank_analysis import time_info

def perform_dank_action(action):
    payload = {"content": f"pls {action}"}
    requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers={"authorization": discord_token})
    print(f"{action} executed {i + 1} times")

def automate_coin_collection(repeat_count, action_list):
    for i in range(repeat_count):
        for action in action_list:
            perform_dank_action(action)
        completed_executions += len(action_list)
        time.sleep(35)

# Replace "Token here" with your actual Discord bot token
discord_token = "Token here"
channel_id = int(input("Input Discord channel ID: "))

# Call the function to display estimated time
total_executions = int(input("Input the total number of planned executions: "))
completed_executions = 0
actions_list = ['fish', 'hunt', 'dig', 'beg']

time_info(total_executions, completed_executions)
automate_coin_collection(total_executions, actions_list)
