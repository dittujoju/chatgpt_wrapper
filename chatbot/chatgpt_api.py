import openai

class ChatGPT:


    def __init__(self, api_key):
        openai.api_key = api_key


    def ask(self, message):
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}]
        )
        return response.choices[0].message.content
