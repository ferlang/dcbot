import discord
from discord.ext import commands

client = commands.Bot(command_prefix="-")

@client.event
async def on_ready():
    print("Bot Is Ready")
	
@client.command
async def hello(ctx):
	await ctx.send("hi")
	
client.run("NzgzMzQyMzAzMDI3OTIwOTU3.X8ZWXg.mwS23r-PhQPq8SshfmjK-drEhvM")
