import unittest
from slack_bot.slack_client import SlackClient
import os

class TestSlackClient(unittest.TestCase):
    def setUp(self):
        self.client = SlackClient(token=os.getenv("SLACK_BOT_TOKEN"))

    def test_send_message(self):
        response = self.client.send_message("#general", "Test message")
        self.assertIsNotNone(response)

if __name__ == "__main__":
    unittest.main()
