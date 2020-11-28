import discord
from discord.ext import commands
import datetime
import asyncio
import random

class answers(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["Nice", "Variables","9"])
    async def answer(self, ctx):
        randomlist = ['Nice!','Good Job!','Amazing!','Great!']
        randomgif = ['https://i.pinimg.com/originals/19/6c/61/196c61ccdc369b6ca39348695fa514cc.gif', 'https://media4.giphy.com/media/cImlpyiQSssyeAVspB/giphy.gif?cid=ecf05e47cb95015479b94c30ac2b10a89cbcd41a2bd10d7b&rid=giphy.gif', 'https://media4.giphy.com/media/hrXNZuo6SYYx079zvd/giphy.gif?cid=ecf05e47516d6a6ab3ba77fa6869fe2355edb0880f58860c&rid=giphy.gif',]
        
        embed = discord.Embed(title="You got it right!", color=0x0a0505, timestamp=ctx.message.created_at)
        embed.add_field(name="Hey,", value=random.choice(randomlist))
        embed.set_thumbnail(url= 'https://i.imgur.com/wYqXOxj.png')
        embed.set_image(url= (random.choice(randomgif)))
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(answers(client))