import discord
from discord.ext import commands

client = commands.Bot(command_prefix="-")

@client.event
async def on_ready():
    print("Bot Is Ready")
	
@client.command
async def hello(ctx):
	await ctx.send("hi")
	
client.run("NzgzMzI0MzQ4NTY2OTk0OTk1.X8ZFpg.CQm9wfprpCf8F6uc2PN9DzNF7tA")
