



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
  
  
@bot.command(pass_context=True)
async def opensource(ctx):
  await bot.say("github.com/ColePZ/stealfeh-python/")
  
  
@bot.command(pass_context=True)
async def dankmemes(ctx):
  await bot.say("Shut up")

  
@bot.command(pass_context=True)
async def info(ctx):
  await bot.say("Stealfeh by Team CC | Discord.py | s!devinfo for Developer Infomation")
  
  
@bot.command(pass_context=True)
async def devinfo(ctx):
  await bot.say("Team CC is a programming group organized by ColePZ and cat939 and they create different projects with the help of many peoples")

  
@bot.command(pass_context=True)
async def helpline(ctx):
  await bot.say("Go else where if u want help im just called this")
  
  
@bot.command(pass_context=True)
async def lol(ctx):
  await bot.say("lol")
  
  
@bot.command(pass_context=True)
async def hello(ctx):
  await bot.say(":wave:")
  
bot.run("Token-Here")
