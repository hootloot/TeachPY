import discord
from discord.ext import commands
import random
import os
import requests
import sys

#non-important stuff

x = 'https://i.imgur.com/wYqXOxj.png'

TOKEN = 'BOT TOKEN'

client = commands.Bot(command_prefix = 'p.')

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Streaming(name = 'ur mom', url = 'https://youtu.be/dQw4w9WgXcQ'))

#cogs

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#info slide

@client.command(name="info")
async def mod(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    embed = discord.Embed(color=0x6707df, timestamp=ctx.message.created_at, title="Learn the Basics of Python")
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.add_field(name="The Print Statement and Variables", value="Learn about print('hello), and Varaiables \n**ex.** `p.print`", inline=False)
    embed.add_field(name="Data Types", value="Learn about the different data types \n**ex.** `p.data`", inline=False)
    embed.add_field(name="Input", value="Learn about the basics of input \n**ex.** `p.input`", inline=False)
    embed.add_field(name="Arithmetic Operators", value="Displays the info of desired user \n**ex.** `p.art`", inline=False)
    embed.add_field(name="String Methods", value="Deletes any desired amount of messages \n**ex.** `p.string`", inline=False)
    embed.add_field(name="Conitional Operators", value="Learn simple conditional operators \n**ex.** `p.con`", inline=False)
    embed.add_field(name="Chained Conditionals", value="Learn about the other Chained Conditionals \n**ex.** `p.chained`", inline=False)
    embed.add_field(name="List and Tuples", value="Leanr about the simple structure of Lists and Tuples \n**ex.** `p.list`", inline=False)
    embed.add_field(name="If and Elif Statements", value="Learn about the important structure of if and elif statements \n**ex.** `p.ifif`", inline=False)
    embed.set_thumbnail(url = x)

    await ctx.send(embed=embed)


#The First Part is Print (Ryan Kim/Hoot Loot)
#Begining of the first part

@client.command(name="print")
async def print(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    embed = discord.Embed(color=0x5207df, timestamp=ctx.message.created_at, title="The Print Statement and Variables")
    embed.set_footer(text=f"Hello, {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.add_field(name="Print", value="The print statement is simple. When you want to output something, write: \n`print('hello world')`", inline=False)
    embed.add_field(name="Variables", value="Variables are an example of a way to give somehing a nickname. Such as: \n`x = 6 \nprint(x)`", inline=False)
    embed.set_image(url= 'https://cdn.discordapp.com/attachments/629132239967354892/781269562971652116/unknown.png')
    embed.set_thumbnail(url = x)

    await ctx.send(embed=embed)

#data types

@client.command(name="data")
async def data(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    embed = discord.Embed(color=0x5207df, timestamp=ctx.message.created_at, title="Different Data Types")
    embed.set_footer(text=f"Hello, {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.add_field(name="String", value="The print statement is simple. When you want to output something, write: \n`print('hello world')`", inline=False)
    embed.add_field(name="Int", value="Numbers that do not a decimal are Int. Such as: \n`-2620, -6789`", inline=False)
    embed.add_field(name="Float", value="Numbers that do have decimal are called Floats. Such as \n`2756.0, -97.8`", inline=False)
    embed.add_field(name="Bool", value="Bools are always: \n`True, or, False`", inline=False)
    embed.set_image(url= 'https://media.discordapp.net/attachments/629132239967354892/781269735626375218/unknown.png')
    embed.set_thumbnail(url = x)

    await ctx.send(embed=embed)

#input and output

@client.command(name="input")
async def input(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    embed = discord.Embed(color=0x5207df, timestamp=ctx.message.created_at, title="Input")
    embed.set_footer(text=f"Hello, {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.add_field(name="Input", value="The input command is very simple, it takes the user's input to output something: \n`x = input('name:')` \n `print(x)`", inline=False)
    embed.set_image(url= 'https://cdn.discordapp.com/attachments/629132239967354892/781269809525686293/unknown.png')
    embed.set_thumbnail(url = x)

    await ctx.send(embed=embed)

#Arithmetic Operator

@client.command(name="art")
async def art(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    embed = discord.Embed(color=0x5207df, timestamp=ctx.message.created_at, title="Different Arthmetic Operator")
    embed.set_footer(text=f"Hello, {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.add_field(name="Look at these examples of Arthmetic Operators", value="+, -, x, ÷", inline=False)
    embed.set_image(url= 'https://media.discordapp.net/attachments/629132239967354892/781294879673942026/unknown.png')
    embed.set_thumbnail(url = x)

    await ctx.send(embed=embed)

#String Methods

@client.command(name="string")
async def string(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    embed = discord.Embed(color=0x5207df, timestamp=ctx.message.created_at, title="Different String Methods")
    embed.set_footer(text=f"Hello, {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.add_field(name="There are many simple string methods, but let's look at the basic ones", value = 'String Methods:', inline=False)
    embed.set_image(url= 'https://cdn.discordapp.com/attachments/629132373203615745/782024877641039882/unknown.png')
    embed.set_thumbnail(url = x)

    await ctx.send(embed=embed)

@client.command(name="con")
async def con(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    embed = discord.Embed(color=0x5207df, timestamp=ctx.message.created_at, title="Different Conditional Operators")
    embed.set_footer(text=f"Hello, {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.add_field(name="It's time to look at the different Conditional Operators", value="lets go!", inline=False)
    embed.set_image(url= 'https://media.discordapp.net/attachments/629132373203615745/782026913664729098/unknown.png')
    embed.set_thumbnail(url = x)

    await ctx.send(embed=embed)

@client.command(name="list")
async def list(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    embed = discord.Embed(color=0x5207df, timestamp=ctx.message.created_at, title="Lists and Tuples")
    embed.set_footer(text=f"Hello, {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.add_field(name="These are just simple examples of Lists and Tuples", value="lets go!", inline=False)
    embed.set_image(url= 'https://cdn.discordapp.com/attachments/629132373203615745/782029035517509632/unknown.png')
    embed.set_thumbnail(url = x)

    await ctx.send(embed=embed)

@client.command(name="ifif")
async def ifif(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    embed = discord.Embed(color=0x5207df, timestamp=ctx.message.created_at, title="if, elif and else statements")
    embed.set_footer(text=f"Hello, {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.add_field(name="Lets find out what if, elif and else statements can do in our code", value="Example:", inline=False)
    embed.set_image(url= 'https://cdn.discordapp.com/attachments/629132373203615745/782030207628476456/unknown.png')
    embed.set_thumbnail(url = x)

    await ctx.send(embed=embed)


client.run(TOKEN)
