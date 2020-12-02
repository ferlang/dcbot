import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print("Bot1 Is Ready")
	
@client.command
async def hello(ctx):
	await ctx.send("hi")
	
client.run(os.environ['DISCORD_TOKEN'])
