import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("Bot1 Is Ready")
	
@client.command()
async def hy(ctx):
	await ctx.send("Hello")
	
client.run(os.environ['DISCORD_TOKEN'])
