import discord
from privateToken import Discord_api_K3y
from privateToken import openAI_api_k3y
import requests
import json


def model_list():
    list = {1: "gpt-3.5-turbo", 2: "gpt-4", 3: "text-davinci-003"}
    return list


model = model_list()[1]
max_messages = 8
conversation = [
                {"role": "system", "content": "You answer questions based on a provided context."}
                # {"role": "assistant", "content": ""}
                # {"role": "user", "content": ""}
                # {"role": "user", "content": str(message.content)}
                ]

# Set the endpoint URL
url = "https://api.openai.com/v1/chat/completions"

# Set the headers
headers_request = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openAI_api_k3y()}"
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
            "messages": conversation,
            "n": 1
            # "max_tokens" : not set (integer)
        }
        
        def update_conversation_history(conversation, new_message):
            conversation.append(new_message)
            if len(conversation) > max_messages:
                for delete in range(1,3):
                    conversation.pop(delete)
                # conversation.pop(1)
                # conversation.pop(2)
                    
        new_message = {"role": "user", "content": str(message.content)}
        update_conversation_history(conversation, new_message)
                
        # Send the POST request
        response = requests.post(url, headers=headers_request, json=payload)
        
        # Get the response JSON data, arrange JSON data with JSON Module
        json_data = response.json()
        print(json.dumps(json_data, indent=4))
        print(len(conversation))

        chatjipiti_answer = json_data["choices"][0]["message"]["content"]
        await message.channel.send(chatjipiti_answer)
        conversation.append({"role": "assistant", "content": chatjipiti_answer})
        
        await message.channel.send(f'Total tokens : {json_data["usage"]["total_tokens"]}')

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(Discord_api_K3y())
