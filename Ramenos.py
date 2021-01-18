#Ramenos.py
#the frog god of discord

import discord
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

#dnd5e api
url = "https://www.dnd5eapi.co/api/"
frogpit = "./images/Frogpit.png"

#Token provided by discord
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
CHANNEL = os.getenv('DISCORD_CHANNEL_ID')

client = discord.Client()

frog_sacrifice_count = 0

#Ramenos demands sacrifices
async def sacrificeFrog(frog_sacrifice_count):
    return f'Another frog has been sacrificed to the SLUMBERING GOD, {frog_sacrifice_count} frogs have been sacrficed! RAMENOS DEMANDS MORE!'

#gets spell from  dnd5e api and turns the return into a string
async def getSpell(content):
    api_call = "-".join(content).lower()
    api_return = requests.get(f'{url}/spells/{api_call}')
    json_api = json.loads(api_return.text)
    if "error" in json_api:
        print(api_return.text)
        return "YOU FOOL! RAMENOS DOES NOT KNOW THAT SPELL!"
    message=f"{json_api['name']}\nSpell Level: {json_api['level']}\nCasting Time: {json_api['casting_time']}\nRange: {json_api['range']}\nComponents: {json_api['components']}"
    if "M" in json_api['components']:
        message+=f"\nMaterials: {json_api['material']}"
    if json_api['ritual']:
        message+=f"\nRitually Castable"
    if json_api['concentration']:
        message+=f"\nRequires Concentration"
    message += f"\n{json_api['desc']}"
    return message

#on set up
@client.event
async def on_ready():
    print(f'{client.user} has logged in')


#listens for messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('Praise Ramenos'):
        await message.channel.send('Your Praise sustains me')
    if message.content.startswith('#Sacrifice'):
        global frog_sacrifice_count 
        frog_sacrifice_count += 1
        count= await sacrificeFrog(frog_sacrifice_count)
        await message.channel.send(count)
    if message.content.startswith('#Ramenos cast'):
        spell = await getSpell(message.content.split(" ")[2:])
        #if spell length under 2000chars print full string, else break it up into chunks
        
        if len(spell) < 2000:
            if spell == "YOU FOOL! RAMENOS DOES NOT KNOW THAT SPELL!":
                await message.channel.send(file=discord.File(frogpit))
            await message.channel.send(spell)
        else:
            for i in range(0,len(spell), 1500):
                await message.channel.send(spell[i:i+1500])
        



client.run(TOKEN)