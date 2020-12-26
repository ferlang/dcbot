import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = ".")

async def my_task(ctx, username):
    while True:
        await ctx.send("Hello")
        await asyncio.sleep(10)

@client.command()
async def info(ctx, username):
    client.loop.create_task(my_task(ctx, username))

@client.event
async def on_ready():
    print("Bot1 Is Ready")

@client.event
async def on_message(message):
    bad_words = ["bad", "stop", "45"]
    for word in bad_words:
        if message.content.count(word) > 0:
            print("A bad word was said")
            await message.channel.purge(limit=1)
	
@client.command()
async def hy(ctx):
	await ctx.send("Hello")
	
client.run(os.environ['DISCORD_TOKEN'])
