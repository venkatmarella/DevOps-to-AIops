from .jira import JiraClient
from .github import GitHubClient
from .terraform import TerraformManager
from .openai_integration import OpenAIClient

class TaskEngine:
    def __init__(self):
        self.jira_client = JiraClient()
        self.github_client = GitHubClient()
        self.terraform_manager = TerraformManager()
        self.openai_client = OpenAIClient()

    def process_command(self, command):
        if "create jira ticket" in command:
            return self.jira_client.create_ticket(command)
        elif "create pr" in command:
            return self.github_client.create_pull_request(command)
        elif "provision" in command:
            return self.terraform_manager.provision_resource(command)
        elif "generate code" in command:
            return self.openai_client.generate_code(command)
        else:
            return "Unknown command"
