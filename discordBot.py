import discord
import random

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
    	if message.content.startswith('$yo'):
    		await message.channel.send("YO")

client = MyClient()
client.run('ODIxMzI1NzMyMDg0MTg3MTc2.YFCFMg.dtKCQmVF-2P8NRLZueoDWjSWoZE')
