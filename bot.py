# next steps: format return arr in get_objects properly, consider using specific coordinate positions

# import required libaries
import discord
import os
from dotenv import load_dotenv
from main import ComputerVision

# create image detection object instance
detector = ComputerVision()

load_dotenv() # loading bot token from .env file
BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

class ListenerBot(discord.Client):
    
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(intents=intents) # make sure we inherit the init of discord.Client as well as its methods

    async def on_ready(self):
        general_channel_id = self.get_channel(1345218942028873840)
        await general_channel_id.send(f"Waiting for image.", tts=True)

    async def on_message(self, message):

        if message.author == self.user: # do not do anything with bot's own messages
            return

        if message.content.lower() == "help":
            await message.reply(content="To take an image, press the 'plus' icon on the bottom left of the screen, the press the camera icon.", tts=True)
        
        if message.attachments != []:
            url = message.attachments[0].url
            await message.reply(content=detector.get_objects(url, showimage=False), tts=True) # await basically allows other functions to run at the same time
            await message.channel.send("Waiting for image.", tts=True)
                                                                                           
bot = ListenerBot()
bot.run(BOT_TOKEN)
