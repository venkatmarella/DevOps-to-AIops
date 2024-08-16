import openai
import os

class OpenAIClient:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def generate_code(self, prompt):
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
