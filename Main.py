#Command to run this file: python3 Main.py

import os
import time
import schedule
import logging
from slack_sdk import WebClient
from pathlib import Path
from dotenv import load_dotenv
from WellBeingBot import *

#code to overcome certificate/unverified SSL error
# https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
logging.basicConfig(level=logging.DEBUG)

# Setup Credentials
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
slack_token = os.environ["SLACK_BOT_TOKEN"]
client = WebClient(slack_token)

#post message to test channel
# client.chat_postMessage(channel="#random", text="Hello World")

# Initialize Well Being Bot
wellBeingBot = WellBeingBot()

# Add members to the Well Being Bot
def save_users(users_array):
    # For testing
    #client.chat_postMessage(channel="#random", text="These are our members: ")
    for user in users_array:
        # Key user info on their unique user ID
        user_id = user["id"]
        user_real_name = user["real_name"]

        # For testing purposes
        #client.chat_postMessage(channel="#random", text=user["real_name"])

        # Store the user in the bot
        wellBeingBot.add_user(user_id, user_real_name)

try:
    # Call the users.list method using the WebClient
    # users.list requires the users:read scope
    result = client.users_list(channel = "C02GAUEAGCU") #random channel: C02GAUEAGCU
    save_users(result["members"])

except SlackApiError as e:
    logger.error("Error creating conversation: {}".format(e))

print("------------------------------------------TEST")

# After every 10mins  is called. 
#schedule.every(1).minutes.do(wellBeingBot.printOutTasks)

# Loop so that the scheduling task
# keeps on running all time.
response = client.conversations_history(channel = "C02G8PBQNBC") #C02G8PBQNBC general
for message in response["messages"]:
    print("Message Content: " + str(message["text"]))
    print("Time sent: " + str(message["ts"]))
# test = test["messages"]

# print(test)

while True:
  
    # Checks whether a scheduled task 
    # is pending to run or not
    response = client.conversations_history(channel = "C02G8PBQNBC") #C02G8PBQNBC general
    for message in response["messages"]:
                if message["ts"] > lastTimeCalculated: #and  check if message is sent from bot?
                    wellBeingBot.calculation(client.reactions_get(     PARAMETERS?       ))
        #print("Message Content: " + str(message["text"]))
        #print("Time sent: " + str(message["ts"]))

    task = wellBeingBot.send_wellnesstask()
    client.chat_postMessage(channel="#general", text=task)
    time.sleep(10)
