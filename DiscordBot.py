

import os
import random
import discord #Allows for work with discord.py
from dotenv import load_dotenv #Allows to load environmental variables
from PIL import Image


intent = discord.Intents.default()
intent.members = True #Allows to use member info from guild

load_dotenv()
botTOKEN = os.getenv('DIMPLE_TOKEN') #Retrieving environmental variables
Guild = os.getenv('DISCORD_GUILD')
client = discord.Client(intents = intent) #Making the connection and using default intents
channel = client.get_channel(client.get_all_channels())



@client.event #Event handler using decorater
async def on_ready():

    guild = discord.utils.get(client.guilds, name = Guild)

    print(f'{client.user} has connected to {guild.name} with the ID: {guild.id}!')


    member_list = []
    for member in guild.members:
        member_list.append(member.name)
    member_list = "\n".join(member_list)
    print(member_list)

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Dimple welcomes you {member.name}!'
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    pic = Image.open("DeezNuts.gif")
    reply = ["I said you a little bitch", "Fight me!", "Im gonna pop one in your ass"]
    if message.content == "GIF":
        rep = pic
        await channel.send(file=discord.File('DeezNuts.gif'))
    emoji = [":tired_face:",":grinning:"]
    if message.content == "How are you feeling Dimple?":
        feelings = random.choice(emoji)
        await message.channel.send(feelings)

    if message.content == "Say what":
        response = random.choice(reply)
        await message.channel.send(response)

client.run(botTOKEN)

