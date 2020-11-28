import discord
from discord.ext import commands
import datetime
import asyncio
import random

class questions(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('bot is online')

    @commands.command()
    async def printq(self, ctx):
        randomlist = ['You can always check the informtion slide from before!','Check back to see the print statement!','Remember what you learned about variables and print statements',]
        randomimage = ['https://cdn.discordapp.com/attachments/706576689844715581/782008220025356288/1964E992-F019-4F9D-BD2F-0BD885373149.jpeg',
        'https://cdn.discordapp.com/attachments/706576689844715581/782008222495146015/902BF53F-F328-465B-9126-A8D15A68CD5E.jpeg',
        'https://cdn.discordapp.com/attachments/706576689844715581/782008226275000350/EEF17097-7661-48B5-B233-413BF7543E3D.jpeg']
        
        embed = discord.Embed(title="Let's see if you can solve this:", color=0x0a0505, timestamp=ctx.message.created_at)
        embed.add_field(name="Good luck,", value=random.choice(randomlist))
        embed.set_image(url= (random.choice(randomimage)))
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url='https://i.imgur.com/wYqXOxj.png')
        
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(questions(client))