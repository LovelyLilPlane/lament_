import discord 
import os
import select
from discord.ext import commands
bot = commands.Bot(command_prefix="`")

for filename in os.listdir('./func'):
    if filename.endswith('.py'):
        bot.load_extension(F'func.{filename[:-3]}')
        
@bot.command()
async def reload(ctx, ext):
    bot.reload_extension(F'func.{ext}')
    await ctx.send(F'{ext} reloaded.')
        
tok = 'OTMzNzExNDYyMTY0MjM0Mjcw.GVaFBX.S-7OHx2v-UpfqaNUGxiWkozv3ch-iZffIEnXjM'
if __name__ == "__main__": 
    bot.run(tok)