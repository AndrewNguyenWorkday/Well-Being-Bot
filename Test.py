import os
import time
import schedule
import logging
from slack_sdk import WebClient
from pathlib import Path
from dotenv import load_dotenv
#from WellBeingBot import *

#code to overcome certificate/unverified SSL error
# https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
logging.basicConfig(level=logging.DEBUG)


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
slack_token = os.environ["SLACK_TOKEN"]
client = WebClient(slack_token)
#Command to run this file: python3 Main.py

#post message to test channel
# client.chat_postMessage(channel="#random", text="Hello World")

# Initialize Well Being Bot 
#wellBeingBot = WellBeingBot()

# Put users into the dict
def save_users(users_array):
    for user in users_array:
        # Key user info on their unique user ID
        user_id = user["id"]
        print(user_id)
        print(user["real_name"])
        # Store the entire user object (you may not need all of the info)
        users_store[user_id] = user

# You probably want to use a database to store any user information ;)
users_store = {}

try:
    # Call the users.list method using the WebClient
    # users.list requires the users:read scope
    result = client.users_list()
    #print(result)
    save_users(result["members"])

except SlackApiError as e:
    logger.error("Error creating conversation: {}".format(e))

