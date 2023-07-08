# Discord-jipity Progress

- &#9745; OpenAI model list added, including GPT3.5 turbo, GPT-4, and text-davinci-003.
- &#9745; Direct API request implemented without importing/using the OpenAI module.
- &#9744; Chat History / Remember previous conversation
- &#9744; GUI for exe file (user input box : openai key, discord bot api key)

## OpenAI Model List

The Discord-jipity project now supports the following OpenAI models:

- GPT3.5-turbo
- GPT-4
- text-davinci-003

To use any of these models, refer to the project documentation for further instructions.

## Direct API Request

API requests to OpenAI without importing or using the OpenAI module. This provides more flexibility and control over the integration process. Detailed documentation on how to make direct API requests will be provided soon.

## Chat History / Remember Previous Conversation

This feature is currently under development. The ability to store and recall chat history will be added in future updates.

## Private Token Configuration

This guide explains how to configure the `privateToken.py` file in your project to store and access your API keys securely.

### Steps

1. Create a new file named `privateToken.py` in the project directory.

2. Copy the code below, replace the values `'YOUR_KEY'` with your actual API keys.

   ```python
   def Discord_api_K3y():
       token = 'YOUR_DISCORD_API_KEY'
       return token

   def openAI_api_k3y():
       secret = 'YOUR_OPENAI_API_KEY'
       return secret

