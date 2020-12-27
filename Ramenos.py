#Ramenos.py
#the frog god of discord

import discord
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()



#Token provided by discord
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
CHANNEL = os.getenv('DISCORD_CHANNEL_ID')

client = discord.Client()
frog_sacrifice_count = 0

async def sacrificeFrog(frog_sacrifice_count):
    return f'Another frog has been sacrificed to the SLUMBERING GOD, {frog_sacrifice_count} frogs have been sacrficed! RAMENOS DEMANDS MORE!'

#on set up
@client.event
async def on_ready():
    print(f'{client.user} has logged in, {frog_sacrifice_count}')


#listens for messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello')
    if message.content.startswith('$Sacrifice'):
        global frog_sacrifice_count 
        frog_sacrifice_count += 1
        count= await sacrificeFrog(frog_sacrifice_count)
        await message.channel.send(count)
    if message.content.startswith('$Ramenos cast'):
        print(message)
        api_return = requests.get(f'https://www.dnd5eapi.co/api/classes/wizard')
        print(api_return.text)
        #await message.channel.send(api_return.text)

client.run(TOKEN)