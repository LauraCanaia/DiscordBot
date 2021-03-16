import discord
import random
import os
from dotenv import load_dotenv
from discord.utils import get

load_dotenv()

class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged on as {0}!'.format(self.user))
		await self.get_channel(821334437324914690).send('Welcome on CoinFlip Bot OwO\nIf you wanna know all the commands of this bot digit $help')
	async def on_message(self, message):
		if message.content.startswith('$help'):
			await message.channel.send('\nHELP:\n$yo = sends you a yo back,\n$flip = flips a coin\n')
		if message.content.startswith('$yo'):
			#await message.channel.send(self.get_user('163718663491420160').name)
			await message.channel.send('\nHELP:\n$yo = sends you a yo back,\n$flip = flips a coin\n')
		if message.content.startswith('$flip'):
			number = random.randint(0,1)
			if(number == 0):
				await message.channel.send("Se sei ronco hai perso")
			else:
				await message.channel.send("Head")

client = MyClient()
client.run(os.environ.get("KEY"))