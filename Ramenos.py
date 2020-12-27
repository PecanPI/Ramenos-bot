#Ramenos.py
#the frog god of discord

import discord
import os
from dotenv import load_dotenv
load_dotenv()

#Token provided by discord
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
CHANNEL = os.getenv('DISCORD_CHANNEL_ID')

client = discord.Client()



#on set up
@client.event
async def on_ready():
    print(f'{client.user} has logged in')


#listens for messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello')

client.run(TOKEN)