#Command to run this file: python3 Main.py

import os
import time
import schedule
import logging
import re
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


'''
general: C02G8PBQNBC 
random channel: C02GAUEAGCU
test: C02GAFV39K7
'''
CHANNEL_ID = "C02GAFV39K7"
BOT_ID = "U02FU4B08CX"

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
    result = client.users_list(channel = CHANNEL_ID) 
    save_users(result["members"])

except SlackApiError as e:
    logger.error("Error creating conversation: {}".format(e))

print("------------------------------------------TEST")

# After every 10mins  is called. 
#schedule.every(1).minutes.do(wellBeingBot.printOutTasks)

# Loop so that the scheduling task
# keeps on running all time.
response = client.conversations_history(channel = CHANNEL_ID) 
# for message in response["messages"]:
#     print("Message Content: " + str(message["text"]))
#     print("Time sent: " + str(message["ts"]))
# test = test["messages"]

# print(test)




#init variable
lastTimeCalculated = 0

#schedule announceResults: final point totals, reset point values
#schedule.every(1).minutes.do(wellBeingBot.announceResults)

#Schedule 
# - announceResults : announces top 3, resets all scores to zero
# - sendWellnessTask: outputs random wellness task 
# <IF TIME ALLOWS> - sendPointUpdate: outputs all scores

#T
#task
#task
#update
#task
# announceResults


 # task ==(30 seconds)==> calculate points => x2 ==> Annouce Results

while True:
  
    # Checks whether a scheduled task 
    # is pending to run or not
    
    newLastTimeCalculated = 0
    # need to update lasttimecalculated
    response = client.conversations_history(channel = CHANNEL_ID) 
    for message in response["messages"]:
                #if new message from bot, get reactions to specific message and give out points to users
        if float(message["ts"]) > lastTimeCalculated and message["user"] == BOT_ID and "reactions" in message.keys():
       # print(message["reactions"] )
            for reaction in message["reactions"]:
           # print(reaction['users'])
                for user in reaction["users"]:
                    wellBeingBot.add_points(user, points = 10)
                    print(wellBeingBot.users_to_points)
            if float(message["ts"]) > newLastTimeCalculated: 
                newLastTimeCalculated = float(message["ts"])
        elif float(message["ts"]) > lastTimeCalculated and "files" in message.keys():
            wellBeingBot.add_points(message["user"], points = 80)
            if float(message["ts"]) > newLastTimeCalculated: 
                newLastTimeCalculated = float(message["ts"])

    lastTimeCalculated = newLastTimeCalculated    

    task = wellBeingBot.send_wellnesstask()
    #client.chat_postMessage(channel="#general", text=task)
    #time.sleep(10)
    #print(wellBeingBot.announceResults())
    break

''' Photo Reaction Conditions 
        elif message["type"] == "file" and message["type"]["timestamp"] > lastTimeCalculated and
            message["type"]["user"] == != BOT ID:  
'''
