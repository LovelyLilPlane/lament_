from genericpath import exists
import discord 
import os
import time
from bs4 import BeautifulSoup
import random
from discord.ext import commands
from core.classes import Cog_ext
import  json, ssl, urllib.request
from opencc import OpenCC
import re
import asyncio
from typing import Union

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class em(Cog_ext):
    @commands.command()
    async def em(self, ctx):
        embed=discord.Embed()
        embed.add_field(name="2", value="2", inline=False)
        embed.add_field(name="2", value="2", inline=True)
        embed.set_image(url = 'https://i.imgur.com/AfFp7pu.png')
        await ctx.send(embed=embed)
    @commands.command(name="reactiontest")    
    async def rtest(self,ctx): # waiting for reactions (✅, ❌) here
        await ctx.send(f"**{ctx.author}**, please react with :white_check_mark: or :x: on this message in 60 seconds")
    
        def check(r: discord.Reaction, u: Union[discord.Member, discord.User]):  # r = discord.Reaction, u = discord.Member or discord.User.
            return u.id == ctx.author.id and r.message.channel.id == ctx.channel.id and \
                str(r.emoji) in ["\U00002705", "\U0000274c"]
        try:
            reaction, user = await self.bot.wait_for(event = 'reaction_add', check = check, timeout = 60.0)
        except asyncio.TimeoutError:
            await ctx.send(f"**{ctx.author}**, you didnt react with a ✅ or ❌ in 60 seconds.")
            return
        else:
            if str(reaction.emoji) == "\U00002705":
                return await ctx.send(f"{ctx.author} reacted with a ✅")
            if str(reaction.emoji) == "\U0000274c":
                return await ctx.send(f"{ctx.author} reacted with a ❌")

def setup(bot):
    bot.add_cog(em(bot))