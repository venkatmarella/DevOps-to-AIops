import unittest
from task_engine.engine import TaskEngine

class TestTaskEngine(unittest.TestCase):
    def setUp(self):
        self.engine = TaskEngine()

    def test_process_command_jira(self):
        response = self.engine.process_command("create jira ticket")
        self.assertIn("Jira ticket created", response)

    def test_process_command_github(self):
        response = self.engine.process_command("create pr")
        self.assertIn("GitHub pull request created", response)

    def test_process_command_terraform(self):
        response = self.engine.process_command("provision")
        self.assertIn("Resource provisioned", response)

    def test_process_command_openai(self):
        response = self.engine.process_command("generate code")
        self.assertIn("def", response)

if __name__ == "__main__":
    unittest.main()
