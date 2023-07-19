## Discord-jipity Progress
This checklist represents the progress I made so far on the Discord-jipity project. The project focuses on integrating OpenAI models into a Discord bot for enhanced chat functionality. The following tasks have been completed or are currently in progress:


| Task                                         | Status |            | Description |
|----------------------------------------------|--------|------------|-------------|
| OpenAI model list                             | &#9745;     |
| Direct API request without using OpenAI module| &#9745;     |
| Chat History / Remember previous conversation | &#9745;     |      | v1 &#9745;
| The Ability to edit message                   | &#9745;     |
| Discord max length character (2000) 'hacks'   | &#9744;     |
| Store appended chat as JSON                   | &#9744;     |
| "Temperature" button inside Discord           | &#9744;     |
| "Max length" button inside Discord            | &#9744;     |
| COPY button inside Discord chat               | &#9744;     |
| GUI for exe file                              | &#9744;     |
| Langchain Integration                         | &#9744;     |

## OpenAI Model List

The Discord-jipity project now supports the following OpenAI models:

- GPT-3.5-turbo-16k-0613
- GPT-4
- text-davinci-003

To use any of these models, refer to the project documentation for further instructions.

## Direct API Request

API requests to OpenAI without importing or using the OpenAI module. This provides more flexibility and control over the integration process. Detailed documentation on how to make direct API requests will be provided soon.

## Chat History / Remember Previous Conversation

functionality for storing and recalling previous chat conversations.

## Discord max length character
Work in progress to handle splitting messages when they reach the maximum character limit of 2000.

## Store appended chat as JSON
Currently being developed to store chat conversations in JSON format, enabling saving and retrieval of conversations.

## "Temperature" button inside Discord
Future implementation of a button to control the accuracy of GPT responses in Discord.
"Max length" button inside Discord: Planned feature to control the maximum length of GPT responses in Discord.

## COPY button inside Discord chat 
a button for copying the full responses

## GUI for exe file
 In progress, creating a graphical user interface for an executable file with user input boxes for OpenAI key and Discord bot API key.


## Private Token Configuration

This guide explains how to configure the `privateToken.py` file in your project to store and access your API keys securely.

### How To Get Started

1. Create a new file named `privateToken.py` in the project directory.

2. Copy the code below, replace the values `'YOUR_KEY'` with your actual API keys.

   ```python
   def Discord_api_K3y():
       token = 'YOUR_DISCORD_API_KEY'
       return token

   def openAI_api_k3y():
       secret = 'YOUR_OPENAI_API_KEY'
       return secret

