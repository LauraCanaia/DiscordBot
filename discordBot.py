import discord
import random
import os
from dotenv import load_dotenv

load_dotenv()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
    	if message.content.startswith('$yo'):
    		await message.channel.send("YO")

client = MyClient()
client.run(os.environ.get("KEY"))
