import logging
#needed to overcome certificate issue
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
logging.basicConfig(level=logging.DEBUG)

import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

slack_token = os.environ["SLACK_BOT_TOKEN"]
client = WebClient(token=slack_token)

try:
    response = client.chat_postMessage(
        channel="random",
        text="Hello from your app! :tada:"
    )
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["error"]    # str like 'invalid_auth', 'channel_not_found'