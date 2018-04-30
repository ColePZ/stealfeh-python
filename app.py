import discord
from discord.ext import commands
import async

bot = commands.Bot("s!")

@bot.event
async def on_ready():
  print("Ready.")
 
 
 @bot.command(pass_context=True)
 async def ping(ctx):
   await bot.say("Pong")
   
   
 @bot.command(pass_context=True)
 async def test(ctx):
  await bot.say("Hello :wave:")
  
  
  bot.run(TOKEN)
