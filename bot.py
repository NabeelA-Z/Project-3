# next steps: format return arr in get_objects properly, add tts to speak out objects, consider using specific coordinate positions

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
        general_channel_id = self.get_channel(1345218942028873840)
        await general_channel_id.send(f"Waiting for image.")

    async def on_message(self, message):

        if message.author == self.user: # do not do anything with bot's own messages
            return
        
        if message.attachments != []:
            url = message.attachments[0].url
            await message.reply(content=detector.get_objects(url, showimage=False)) # await basically allows other functions to run at the same time
            await message.channel.send("Waiting for image.")
                                                                                           
bot = ListenerBot()
bot.run(BOT_TOKEN)
