
import discord
from privateToken import Discord_api_K3y
from privateToken import openAI_api_k3y
import requests

import sys
from tkinter import *

import threading

import logging
from io import StringIO

import time


# Create a StringIO object to capture log messages as strings
log_stream = StringIO()
handler = logging.StreamHandler(log_stream)

# Configure the logger to capture all log messages from discord and add the handler
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def model_list():
    list = {1: "gpt-3.5-turbo", 2: "gpt-4", 3: "text-davinci-003"}
    return list


model = model_list()[1]

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
            "messages": [{"role": "user", "content": str(message.content)}],
            "n": 1
        }

        # Send the POST request
        response = requests.post(url, headers=headers_request, json=payload)
        # Get the response JSON data
        json_data = response.json()

        chatjipiti_answer = json_data["choices"][0]["message"]["content"]
        await message.channel.send(chatjipiti_answer)


def log_print():
    log_output = log_stream.getvalue()
    print(log_output)


class App(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.build_widgets()
        self.run_script()  # Call the run_script() method immediately after initializing the App

    def run_script(self):
        sys.stdout = self
        self.text1.delete(1.0, END)  # Clear the text area
        log_print()

        current_time = time.strftime("%H:%M:%S")  # Get the current time
        # Update the timer label
        self.timer_label.config(text="Current Time: " + current_time)

        self.after(2000, self.run_script)
        sys.stdout = sys.__stdout__

    def build_widgets(self):
        self.text1 = Text(self)
        self.text1.pack(side=TOP)

        self.timer_label = Label(self, text="Current Time: ")
        self.timer_label.pack(side=TOP)

        self.button = Button(self, text="Trigger script",
                             command=self.run_script)
        # self.button.pack(side=TOP)
        self.button.pack_forget()
        # Hide the button by using either of the following lines:
        # self.button.pack_forget()  # To completely remove the button from the layout
        # self.button.config(state=DISABLED)  # To disable the button, making it grayed out and unclickable

    def write(self, txt):
        self.text1.insert(INSERT, txt)


root = Tk()
app = App(master=root)

# Define your Discord bot code and run it


def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = MyClient(intents=intents)
    client.run(Discord_api_K3y())


# Create a separate thread for running the Discord bot
discord_thread = threading.Thread(target=run_discord_bot)

# Start the Discord bot thread
discord_thread.start()

app.mainloop()
