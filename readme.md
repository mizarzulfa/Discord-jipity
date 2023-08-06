## Discord-jipity Progress
This checklist represents the progress I made so far on the Discord-jipity project. The project focuses on integrating OpenAI models into a Discord bot for enhanced chat functionality. The following tasks have been completed or are currently in progress:


| Task                                         | Status |            | Description |
|----------------------------------------------|--------|------------|-------------|
| OpenAI model list                             | &#10004;     |
| Direct API request without using OpenAI module| &#10004;     |
| Chat History / Remember previous conversation | &#10004;     |      | v1 &#10004;
| The Ability to edit message                   | &#10004;     |
| Discord max length character (2000) 'hacks'   | &#10004;     |
| Store appended chat as JSON                   | &#9744;     |
| "Temperature" button inside Discord           | &#9744;     |
| "Max length" button inside Discord            | &#9744;     |
| COPY button inside Discord chat               | &#9744;     |
| GUI for exe file                              | &#9744;     |
| Langchain Integration                         | &#9744;     |

## OpenAI Model List

The Discord-jipity project supports the following OpenAI models:

- GPT-3.5-turbo-16k-0613
- GPT-4
- text-davinci-003

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

