import openai

import telethon

from telethon import TelegramClient, events

# set up the OpenAI API

openai.api_key = "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"

# set up the Telegram API

api_id = 988074

api_hash = 'a5ec8b7b6dbeedc2514ca7e4ba200c13'
client = TelegramClient('session_name', api_id, api_hash)

# define the event handler for incoming messages

@client.on(events.NewMessage(chats='YOUR_GROUP_CHAT_ID_HERE'))

async def handler(event):

    # check if the message is from @durov

    if event.message.sender.username == 'DawnWithNine':

        # generate a response with GPT-3
        messag = event.message.message
   
        prompt = messag

        response = openai.Completion.create(

            engine="davinci",

            prompt=prompt,

            max_tokens=50

        )

        # send the response to the group

        await event.reply(response.choices[0].text)

# start the bot

client.start()

client.run_until_disconnected()

