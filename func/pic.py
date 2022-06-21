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
def rewrite():
    with open('setting.json', "w") as f1:
        f1.write(str(jdata).replace("\'", "\""))

class pic(Cog_ext):
    @commands.group()
    async def pic(self, ctx):
        pass
    @pic.command()
    async def p(self,ctx,cat,arg):
        if F'{cat}' in jdata:
            if str(arg) in jdata[str(cat)]:
                await ctx.send('the pic is already in this catagory.')
            elif str(arg).startswith('https://'):
                jdata[str(cat)].append(str(arg))
                rewrite()
                await ctx.send('the pic is upload successfully.')
            else:
                await ctx.send('the url isn\'t fit the format.')
        else:
            jdata[str(cat)] = []
            await ctx.send(F'the catagory isn\'t exist yet, the catagory {str(cat)} is genarated now.')
            if str(arg).startswith('https://'):
                jdata[str(cat)].append(str(arg))
                rewrite()
                await ctx.send('the pic is upload successfully.')
            else:
                await ctx.send('the url isn\'t fit the format.')
    @pic.command()
    async def s(self,ctx,cat):
        if F'{cat}' in jdata:
            await ctx.send(random.choice(jdata[str(cat)]))
        else:
            await ctx.send('the catagory isn\'t exist yet, please use ````pic p +catagory +url``` to add the new catagory.')
    @pic.command()
    async def l(self,ctx,cat):
        if str(cat) == 'all':
            tmp = "\n"
            for i in jdata.keys():
                tmp += i + "\n"        
            await ctx.send(F'the following list is all of the catagory in the function. ```{tmp}```')
        else:
            global now_pos
            global now_cat
            now_cat = str(cat)
            now_pos = 0
            embed=discord.Embed(title = F'Catagory:{str(cat)} No.{now_pos+1}', url = F'{jdata[str(cat)][now_pos]}',color = discord.Color.purple()) 
            embed.set_image(url = F'{jdata[str(cat)][now_pos]}')
            msg = await ctx.send(embed = embed)
            #await ctx.send(embed.title)
            emoji = ["\U00002b05", "\U000027a1"] #left and right arrow
            for i in emoji:
                await msg.add_reaction(i)
            def embed_gen(self,cat,now_pos,url):
                embed=discord.Embed(title = F'Catagory:{str(cat)} No.{now_pos+1}', url = url,color = discord.Color.purple()) 
                embed.set_image(url = url)
    @commands.Cog.listener()
    async def on_raw_reaction_add(self,data):
        if len(data.message.embeds) == 0 or data.id == self.bot.user.id: return
        if "Catagory" in str(data.message.embeds.title):
            msg = data.message
            url = data.message.embeds.url
            if str(data.emoji) == "\U00002b05":
                now_pos-=1 
                if now_pos < 0:
                    now_pos = len(jdata[str(now_cat)])-1
                await msg.edit(embed = self.embed_gen(now_cat ,now_pos,url))
                await msg.send('db msg -> passed')
                await msg.remove_reaction(data.reaction, data.user)
            elif str(data.emoji) == "\U000027a1":
                now_pos+=1 
                if now_pos > len(jdata[str(now_cat)])-1:
                    now_pos = 0
                await msg.edit(embed = self.embed_gen(now_cat ,now_pos,url))
                await msg.send('db msg <- passed')
                await msg.remove_reaction(data.reaction, data.user)
            
    
                
        
                
        
        
        

def setup(bot):
    bot.add_cog(pic(bot))