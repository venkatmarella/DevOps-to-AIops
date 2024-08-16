from slack_bolt import App
from task_engine.engine import TaskEngine
import os

# Initialize the Slack app with your bot token
app = App(token=os.getenv("SLACK_BOT_TOKEN"))

# Initialize the task engine
engine = TaskEngine()

@app.command("/aiops")
def handle_aiops_command(ack, respond, command):
    ack()
    response = engine.process_command(command['text'])
    respond(response)

if __name__ == "__main__":
    app.start(port=3000)
