import os

class Config:
    SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
    JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
    GITHUB_API_TOKEN = os.getenv("GITHUB_API_TOKEN")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
