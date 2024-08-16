import os
from github import Github

class GitHubClient:
    def __init__(self):
        self.client = Github(os.getenv("GITHUB_API_TOKEN"))

    def create_pull_request(self, repo_name, branch_name, title, body):
        repo = self.client.get_repo(repo_name)
        pr = repo.create_pull(title=title, body=body, head=branch_name, base="main")
        return f"GitHub pull request created: {pr.url}"
