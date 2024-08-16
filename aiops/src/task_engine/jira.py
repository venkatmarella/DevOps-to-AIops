import os
from jira import JIRA

class JiraClient:
    def __init__(self):
        self.client = JIRA(server="https://your-jira-instance.atlassian.net", basic_auth=("email@example.com", os.getenv("JIRA_API_TOKEN")))

    def create_ticket(self, summary, description, project_key):
        issue_dict = {
            'project': {'key': project_key},
            'summary': summary,
            'description': description,
            'issuetype': {'name': 'Task'},
        }
        issue = self.client.create_issue(fields=issue_dict)
        return f"Jira ticket created: {issue.key}"
