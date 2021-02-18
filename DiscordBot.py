

import os, random #Necessary modules
import discord #Allows for work with discord.py
from dotenv import load_dotenv #Allows to load environmental variables
from datetime import datetime


intent = discord.Intents.default()
intent.members = True #Allows to use member info from guild

load_dotenv()
botTOKEN = os.getenv('DIMPLE_TOKEN') #Retrieving environmental variables
Guild = os.getenv('DISCORD_GUILD')
client = discord.Client(intents = intent) #Making the connection and using default intents
channel = client.get_channel(client.get_all_channels())



@client.event #Event handler using decorater
async def on_ready(): #When dimple is launched
    guild = discord.utils.get(client.guilds, name=Guild) #retrieving guild using discord.py easy to write functions
    print(f'{client.user} has connected to {guild.name} with the ID: {guild.id}!')


@client.event
async def on_member_join(member): #When a member joins
    await member.create_dm() #Cretes a private message and sends it to user
    await member.dm_channel.send(
        f'Dimple welcomes you {member.name}! Say `Help Dimple` in server to see the ways I can assist you'
    )

@client.event
async def on_message(message): #When users sends message
    if message.author == client.user: #To make sure its not a message by bot
        return
    guild = discord.utils.get(client.guilds, name=Guild)  # Obtains the correct server
    if message.content == "Dimple show roles available":
        roles = await guild.fetch_roles()
        for role in roles:
            if role.name == '@everyone':
                continue
            else:
                await message.channel.send("`-" + role.name + "`")
                time.sleep(1)

    Word_check = message.content.split(" ")
    Checker = discord.utils.find(lambda l: l == "!Suggestion", Word_check)
    if Checker != None:
        Word_check.pop(0)
        Word_check = " ".join(Word_check)
        file = open('Suggestion.csv', 'a')
        file.write(f'\n{message.author},{Word_check[0]}')
        file.close()
        await message.channel.send("Thank you! Dimple has received your message.")

    if "Set reminder for" in message.content:
        Terms = message.content.split(" ")

        for i in range(0,3):
            del Terms[0]
        current_time = datetime.now().strftime("%H:%M")
        await message.channel.send(f"Got it! Dimple will remind you at {Terms[0]}:{Terms[1]}")
        while f"{Terms[0]}:{Terms[1]}" != current_time:
            current_time = datetime.now().strftime("%H:%M")
            if f"{Terms[0]}:{Terms[1]}" == current_time:
                break
        await message.channel.send(f"@{message.author.name} ITS YOUR TIME!")






    member_list = ["`Server members are:`"]
    for member in guild.members: #Loop stores members in list
        if member.bot: #Adds bot to bot members
            member_list.append("`-" + member.name + " (Bot)`")
        else:
            member_list.append("`-"+member.name+"`") #Adding members to a list
    member_list = "\n".join(member_list)
    if message.content == "Dimple give me server info":
        await message.channel.send(f"`Number of members: {guild.member_count}`" )
        await message.channel.send(member_list) #Sending out the list


    emoji = [":tired_face:",":grinning:",":disappointed:",":angry:",":neutral_face:"] #Emojis dimple can express
    if message.content == "How are you feeling Dimple?":
        feelings = random.choice(emoji) #Randomely selects emoji
        await message.channel.send(feelings)
    if message.content == "Help Dimple":
        help_options = """Dimple can:
-give server info if you say `Dimple give me server info`
-Tell you how I feel if you say `How are you feeling Dimple?`
-Answer yes/no question if you ask with `Listen` included and add `?` at the end of your question
-Show roles available if you say `Dimple show roles available`
-Can add a suggestion for admin to see if you say `!Suggestion [insert suggestion here]`
-Can set a reminder if time provided in a 24 hour format like `14 02`
"""
        await message.channel.send(help_options)

    reply = [
        "Don't count on it.",
        "My reply is no.",
        "As I see it, yes.",
        "It is certain.",
        "Most likely.",
        "Outlook not so good.",
        "Ask again later.",
        "Better not tell you now."
    ] #For yes/no question

    if message.content:
        words = message.content.split()
        locateListen = discord.utils.find(lambda l: l == "Listen",words)
        locateQuestionMark = discord.utils.find(lambda l: l == "?", words[-1])

        if (locateListen != None and locateQuestionMark != None): #Looks for both listen and a question mark
            response = random.choice(reply)
            await message.channel.send(response)
        elif locateListen != None and locateQuestionMark == None: #If listen is said
            fixPunctuationResponse = "Dimple either doesn't see a question or question mark.\nDon't mess with me!"
            await message.channel.send(fixPunctuationResponse)


client.run(botTOKEN) #Makes the bot run and connects to discord
