import discord
from discord.ext import commands
from bot import Player

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
	print(f"{bot.user.name} is ready")

async def setup():
	await bot.wait_until_ready()
	bot.add_cog(Player(bot))

bot.loop.create_task(setup())
bot.run("")
