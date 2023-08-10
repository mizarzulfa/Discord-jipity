import discord
from privateToken import Discord_api_K3y, openAI_api_k3y
import requests
import json
import argparse

parser = argparse.ArgumentParser(description="Run the Discord bot")
parser.add_argument("--run", action="store_true", help="Run the bot")
args = parser.parse_args()

# Dictionary to store the bot's messages
bot_messages = {}

def model_list():
    list = {
        1: "gpt-3.5-turbo",
        2: "gpt-4-0613",
        3: "text-davinci-003"}
    return list

model = model_list()[2]
max_messages = 8

def update_conversation_history(conversation, new_message):
    conversation.append(new_message)
    if len(conversation) > max_messages:
        for delete in range(1,3):
            conversation.pop(delete)
            # conversation.pop(1)
            # conversation.pop(2)

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

# Set the payload (JSON data)
payload = {
    "model": model,
    "messages": conversation,
    "n": 1
    # "max_tokens" : not set (integer)
}

def response_post():
    # Send the POST request
    response = requests.post(url, headers=headers_request, json=payload)
    # Get the response JSON data, arrange JSON data with JSON Module
    json_data = response.json()
    # print(json.dumps(json_data, indent=4))
    return json_data
        
        
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
                
        new_message = {"role": "user", "content": str(message.content)}
        update_conversation_history(conversation, new_message)
        
        response_post()

        #Chunk messages
        chatjipiti_answer = response_post()["choices"][0]["message"]["content"]
    
        chunk_size = 999
        chunks = [chatjipiti_answer[i:i+chunk_size] for i in range(0, len(chatjipiti_answer), chunk_size)]

        if len(chunks) > 1 and len(chunks[-1]) < chunk_size:
            chunks[-2] += chunks[-1]
            chunks.pop()

        for i, chunk in enumerate(chunks):
            new = chunk
            # print(f"Chunk {i}: {new}")
            bot_response = await message.channel.send(new)
        
        # await message.channel.send(chunks[0])
        conversation.append({"role": "assistant", "content": chatjipiti_answer})
        bot_response2 = await message.channel.send(f'Total tokens : {response_post()["usage"]["total_tokens"]}')
        # Store the bot's messages
        bot_messages[message.author.id] = {
            "response1": bot_response,
            "response2": bot_response2
        }
        

        
    async def on_message_edit(self, before, after):
        global conversation  # Declare conversation as a global variableglobal conversation  # Declare conversation as a global variable
        
        if before.author == self.user:  # Ignore edits made by the bot itself
            return
        
        if before.author.id in bot_messages:
            # Delete the bot's previous responses
            responses = bot_messages[before.author.id]
            await responses["response1"].delete()
            await responses["response2"].delete()
            del bot_messages[before.author.id]
            # if len(conversation) >= 0:
            #     conversation = conversation[:-2]
            if len(conversation) > 0:
                conversation.pop(len(conversation) - 1)  # Remove the last item
                conversation.pop(len(conversation) - 1)  # Remove the new last item after the first removal

            

        # Continue with handling the message edit
        # user = before.author
        # channel = before.channel
        # old_content = before.content
        new_content = after.content

        # Example: Print the details of the edited message
        # print(f"Message edited by {user} in {channel}:")
        # print(f"Old content: {old_content}")
        # print(f"New content: {new_content}")
        
        # new_message = {"role": "user", "content": str(new_content)}
        conversation.append({"role": "user", "content": str(new_content)})
        # new_message = {"role": "user", "content": "1st fifa world cup held?"}
        
        json_data = response_post()
        
        edit_msg_chatjipity_response = json_data["choices"][0]["message"]["content"]
        
        chunk_size = 999
        chunks = [edit_msg_chatjipity_response[i:i+chunk_size] for i in range(0, len(edit_msg_chatjipity_response), chunk_size)]

        if len(chunks) > 1 and len(chunks[-1]) < chunk_size:
            chunks[-2] += chunks[-1]
            chunks.pop()

        for i, chunk in enumerate(chunks):
            new = chunk
            # print(f"Chunk {i}: {new}")
            bot_response = await after.channel.send(new)
            bot_messages[before.author.id] = {"response1": bot_response}
        
        # await message.channel.send(chunks[0])
        conversation.append({"role": "assistant", "content": edit_msg_chatjipity_response})
        bot_response2 = await after.channel.send(f'Total tokens : {json_data["usage"]["total_tokens"]}')
        bot_messages[before.author.id]["response2"] = bot_response2
        print(len(conversation))

def main_x():
    intents = discord.Intents().all()
    client = MyClient(intents=intents)
    client.run(Discord_api_K3y())

if args.run:
    main_x()
    
if __name__ == "__main__":
    print("This script cannot be executed directly.")
    print("It should be imported as a module.")
    print("or run it using argument 'current path file' '--run")