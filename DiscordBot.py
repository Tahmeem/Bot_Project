

import os, random, time #Necessary modules
import discord #Allows for work with discord.py
from dotenv import load_dotenv #Allows to load environmental variables



intent = discord.Intents.default()
intent.members = True #Allows to use member info from guild

load_dotenv()
botTOKEN = os.getenv('DIMPLE_TOKEN') #Retrieving environmental variables
Guild = os.getenv('DISCORD_GUILD')
client = discord.Client(intents = intent) #Making the connection and using default intents
channel = client.get_channel(client.get_all_channels())



@client.event #Event handler using decorater
async def on_ready():
    guild = discord.utils.get(client.guilds, name=Guild)
    print(f'{client.user} has connected to {guild.name} with the ID: {guild.id}!')

"""
    member_list = []
    for member in guild.members:
        member_list.append(member.name)
    member_list = "\n".join(member_list)
    print(member_list)
"""
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Dimple welcomes you {member.name}!'
    )

#role = discord.utils.get(member.server.roles, id = "")
    #await client.add_roles(Lab Rats.Snowflake)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    guild = discord.utils.get(client.guilds, name=Guild) #Obtains the correct server
    member_list = ["`Server members are:`"]
    for member in guild.members:
        if member.bot: #Adds bot to bot members
            member_list.append("`-" + member.name + " (Bot)`")
        else:
            member_list.append("`-"+member.name+"`") #Adding members to a list
    member_list = "\n".join(member_list)
    if message.content == "Dimple give me server info":
        await message.channel.send(f"`Number of members: {guild.member_count}`" )
        time.sleep(1)
        await message.channel.send(member_list) #Sending out the list

    reply = [
        "Don't count on it.",
        "My reply is no.",
        "As I see it, yes.",
        "It is certain.",
        "Most likely.",
        "Outlook not so good.",
        "Ask again later.",
        "Better not tell you now."
    ]


    emoji = [":tired_face:",":grinning:",":disappointed:",":angry:",":neutral_face:"]
    if message.content == "How are you feeling Dimple?":
        feelings = random.choice(emoji)
        await message.channel.send(feelings)


    words = message.content.split()
    locateListen = discord.utils.find(lambda l: l == "Listen",words)
    locateQuestionMark = discord.utils.find(lambda l: l == "?", words[-1])

    if (locateListen != None and locateQuestionMark != None):
        response = random.choice(reply)
        await message.channel.send(response)
    elif locateListen != None and locateQuestionMark == None:
        fixPunctuationResponse = "Dimple either doesn't see a question or question mark.\nDon't mess with me!"
        await message.channel.send(fixPunctuationResponse)

client.run(botTOKEN)

