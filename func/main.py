import discord 
import os
from discord.ext import commands
from core.classes import Cog_ext

class main(Cog_ext):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(F'{round(self.bot.latency*1000)} (ms)')
        
            
def setup(bot):
    bot.add_cog(main(bot))