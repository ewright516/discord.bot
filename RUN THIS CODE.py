import discord
from discord.ext import commands    # imports
from discord.utils import get

token = 'NzEzNDQ3OTAzOTg0NjE1NTU2.Xsih6Q.IOazhA63QZxv4g-obTuKab7G0qo'    # variable definitions
ROLE = "Tester"

client = discord.Client()



@client.event
async def on_message(message):
    message.content = message.content.lower()
    if str(message.channel) == "sharing-with-github" and message.content.startswith("https://github.com"):
        await message.channel.send("Thanks!")
    elif str(message.channel) == "sharing-with-github":         # github censorship
        await message.channel.purge(limit=1)
        
    if message.content.startswith("fuck"):
        await message.channel.purge(limit=1)  # cursing censorship
    if message.content.startswith("nigg"):
        await message.channel.purge(limit=1)
    if message.content.startswith("shit"):
        await message.channel.purge(limit=1)

    if message.content.startswith("~help"):
        await message.channel.send("Sorry, we're working on user commands. Come back soon!")


    message.content = message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("hello bot"):

        if str(message.author) == "SlideZ#6554":
            user = "SlideZ"
            await message.channel.send("Hello creator " + user + "!")
        elif str(message.author) == "Xueren#1671":                        # "Hello Bot" control
            user = "Xueren"
            await message.channel.send("Hello creator " + user + "!")
        elif str(message.author) == "Duck#1044":
            user = "Kevin"
            await message.channel.send("Sup gay boy " + user)
        else:
            await message.channel.send("whats up my ni**a " + str(message.author))
            
client.run(token)