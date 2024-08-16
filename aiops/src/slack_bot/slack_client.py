from slack_sdk import WebClient

class SlackClient:
    def __init__(self, token):
        self.client = WebClient(token=token)

    def send_message(self, channel, text):
        self.client.chat_postMessage(channel=channel, text=text)
