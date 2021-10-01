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


'''
general: C02G8PBQNBC 
random channel: C02GAUEAGCU
test: C02GAFV39K7
hackathon: C02GAUM90R2
'''
CHANNEL_ID = "C02GAUM90R2"
BOT_ID = "U02FU4B08CX"

# Add members to the Well Being Bot
def save_users(users_array):
    # For testing
    #client.chat_postMessage(channel="#random", text="These are our members: ")
    for user in users_array:
        # Key user info on their unique user ID
        # don't add slackbot and WellBeingBot to leaderboard
        #if user["id"] == "USLACKBOT" or user["id"] == BOT_ID:
        #    continue
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

response = client.conversations_history(channel = CHANNEL_ID) 


#init variable
lastTimeCalculated = 0

# Parameters: dictionary ex: {1 : [("User1", 10), ("User3", 10)], 2 : [("User2", 8)], 3 : []}
# Description: Creates output Text
def announceResults(winnerDict):
    # Format the list
    def listToText(users):
        listUsersText = ""
        for i in range(0, len(users)):
            listUsersText += users[i][0] + " (Score: " + str(users[i][1]) + ")"
            if i != len(users) - 1:
                listUsersText += ", "
        return listUsersText

    # Setup Variables
    outputText = "Here are this week's winners!!!! 🥳 🥳 🎉🎉 \n"
    counter = 1

    # Build output text
    while counter <= 3:
        if counter == 1:
            outputText += "1st Place: "
        elif counter == 2:
            outputText += "2nd Place: "
        elif counter == 3:
            outputText += "3rd Place: "
        outputText += listToText(winnerDict[counter])
        
        if counter < 3:
            outputText += "\n"
        counter += 1
    
    client.chat_postMessage(channel=CHANNEL_ID, text=outputText)
Looptwice = 0
while True:
  
    # Send task for users to complete
    task = wellBeingBot.send_wellnesstask()
    client.chat_postMessage(channel= CHANNEL_ID, text=task)

    # Time for users to complete task
    time.sleep(25)
    
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
                
        #points for posting photo        
        elif float(message["ts"]) > lastTimeCalculated and "files" in message.keys():
            wellBeingBot.add_points(message["user"], points =  5)
            if float(message["ts"]) > newLastTimeCalculated: 
                newLastTimeCalculated = float(message["ts"])

                
        #points for users reacting to your message (photo or message)
        if float(message["ts"]) > lastTimeCalculated and message["user"] != BOT_ID and "reactions" in message.keys():
            for reaction in message["reactions"]:
                wellBeingBot.add_points(message["user"], points = reaction["count"])
            if float(message["ts"]) > newLastTimeCalculated:
                newLastTimeCalculated = float(message["ts"])


    # Update oldest timestamp to calculate points for
    lastTimeCalculated = newLastTimeCalculated    

    # Announce Winners based on points
    winnerDict = wellBeingBot.topScores()

    if Looptwice == 0:
        Looptwice += 1
        continue
    else:
        announceResults(winnerDict)    
        break
