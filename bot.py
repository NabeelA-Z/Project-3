import discord
from main import ComputerVision

detector = ComputerVision()

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