import discord
from discord.ext import commands

bot = commands.Bot("s!")

@bot.event
async def on_ready():
  print("Ready.")
 
 
@bot.command(pass_context=True)
async def ping(ctx):
   await bot.say("Pong")
   
   
@bot.command(pass_context=True)
async def test(ctx):
  await bot.say("Working, Ready for use")
  
  
bot.run("Token-Here")
