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
	
@client.command()
async def server(ctx):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)
	
        owner = str(ctx.guild.owner)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        memberCount = str(ctx.guild.member_count)
 
        icon = str(ctx.guild.icon_url)

        embed = discord.Embed(
            title=name + " Server Information",
            description=description,
            color=discord.Color.red()
        )
        embed.set_thumbnail(url_icon)
        embed.add_field(name="owner", value=owner, inline=True)
        embed.add_field(name="Server ID", value=id, inline=True)
        embed.add_field(name="Region", value=region, inline=True)
        embed.add_field(name="Member Count", value=memberCount, inline=True)

        await ctx.send(embed=embed)
	
	
client.run(os.environ['DISCORD_TOKEN'])
