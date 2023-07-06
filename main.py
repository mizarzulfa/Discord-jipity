import discord
from privateToken import myToken
from privateToken import api

import requests


def model_list():
    list = {1: "gpt-3.5-turbo", 2: "gpt-4", 3: "text-davinci-003"}
    return list


model = model_list()[1]

# Set the endpoint URL
url = "https://api.openai.com/v1/chat/completions"

# Set the headers
headers_request = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api()}"
}


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        # Set the payload (JSON data)
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": str(message.content)}],
            "n": 1
        }

        # Send the POST request
        response = requests.post(url, headers=headers_request, json=payload)
        # Get the response JSON data
        json_data = response.json()

        chatjipiti_answer = json_data["choices"][0]["message"]["content"]
        await message.channel.send(chatjipiti_answer)


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(myToken())
