import discord
import os
from dotenv import load_dotenv
from main import ComputerVision

detector = ComputerVision()

load_dotenv() # new to environment variables and os, but hopefully should keep my token safe lol
BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

class ListenerBot(discord.Client):
    
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(intents=intents) # make sure we inherit the init of discord.Client as well as its methods

    async def on_ready(self):
        print(f"Waiting for images.")

    async def on_message(self, message):

        if message.author == self.user: # do not do anything with bot's own messages
            return
        
        if message.attachments != []:
            url = message.attachments[0].url
            print(detector.get_objects(url))

bot = ListenerBot()
bot.run(BOT_TOKEN)
