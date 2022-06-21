import discord 
import os
import time
from bs4 import BeautifulSoup
import random
from discord.ext import commands
from core.classes import Cog_ext
import  json, ssl, urllib.request
from opencc import OpenCC

dic_mode_convert = {26:'王座', 24:'玉', 22:'金', 25:'王座東',23:'玉東',21:'金東'}
cc = OpenCC('s2t')

class random_yakuman(Cog_ext):
    @commands.command()
    async def RY(self,ctx,arg = []):
        mode = random.randrange(21, 26)
        C_mode = dic_mode_convert[mode]
        url = F'https://ak-data-1.sapk.ch/api/v2/pl3/recent_highlight_games?limit=100&mode={mode}'
        context = ssl._create_unverified_context()
        with urllib.request.urlopen(url, context=context) as jsondata:
            data = json.loads(jsondata.read()) 
        ram = random.randrange(101)
        tmp = data[ram]['uuid']
        yk_amount = data[ram]['event']['fan']
        if len(yk_amount) > 1:
            label = ""
            fan_tot = 0
            for i in range(len(yk_amount)):
                label += (yk_amount[i]['label']+ "\n")
                fan_tot += yk_amount[i]['count']
            await ctx.send(F'{C_mode}\n{cc.convert(label)}{fan_tot}番\nhttps://game.maj-soul.com/1/?paipu={tmp}')
        else:
            await ctx.send(F'{C_mode}\n'+cc.convert(yk_amount[0]['label'])+F'\nhttps://game.maj-soul.com/1/?paipu={tmp}')
            
def setup(bot):
    bot.add_cog(random_yakuman(bot))
