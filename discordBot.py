import discord
import random
import os
from dotenv import load_dotenv
from discord.utils import get

load_dotenv()

class MyClient(discord.Client):
	async def on_message(self, message):
		if message.content.startswith('$help'):
			await message.channel.send('\nHELP:\n$yo = sends you a yo back,\n$flip = flips a coin\n')
			
		if message.content.startswith('$flip h'):
			ronco = await client.fetch_user("238685089255391233")
			if message.author == ronco:
				await message.channel.send("Tails! YOU LOST!")
			else:
				number = random.randint(0,1)
				if(number == 0):
					await message.channel.send("Tails! YOU LOST!")
				else:
					await message.channel.send("Head! YOU WON!!")
			
		if message.content.startswith('$flip t'):
			ronco = await client.fetch_user("238685089255391233")
			if message.author == ronco:
				await message.channel.send("Head! YOU LOST!!")
			else:
				number = random.randint(0,1)
				if(number == 0):
					await message.channel.send("Tails! YOU WON!!")
				else:
					await message.channel.send("Head! YOU LOST!")
				
client = MyClient()
client.run(os.environ.get("KEY"))