import sys
import threading
import logging
import time
from tkinter import *
from io import StringIO
import asyncio
from main import main_x as discord_server_run

# a StringIO object to capture log messages as strings
log_stream = StringIO()
handler = logging.StreamHandler(log_stream)

# Configure the logger to capture all log messages from discord and add the handler
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
logger.addHandler(handler)

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
        
        ##default##
        # self.button.pack(side=TOP)
        
        self.button.pack_forget()
        # Hide the button by using either of the following lines:
        # self.button.pack_forget()  # To completely remove the button from the layout
        # self.button.config(state=DISABLED)  # To disable the button, making it grayed out and unclickable

    def write(self, txt):
        self.text1.insert(INSERT, txt)


root = Tk()
app = App(master=root)


def run_discord_bot():
    discord_server_run()

# Create and run the event loop in the separate thread
def discord_thread_func():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_discord_bot())
    loop.close()

# Start the Discord bot thread and TKINTER
def main_GUI():
    discord_thread = threading.Thread(target=discord_thread_func)
    discord_thread.start()
    app.mainloop()
    
if __name__ == "__main__":
    print("This script cannot be executed directly.")
    print("It should be imported as a module.")
