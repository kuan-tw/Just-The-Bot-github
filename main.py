import discord 
from discord.ext import commands
import keep_alive
import os
import asyncio
import datetime
import random
import json
from dotenv import load_dotenv
from discord.utils import get 
import requests



load_dotenv()

token = os.getenv("DISCORD_BOT_SECRET")

intents = discord.Intents.all()

def is_it_me(ctx):
  return ctx.author.id == 536445172247167016 or 542715105276723202
  
bot = commands.Bot(command_prefix='=', intents=intents)
bot.remove_command('help')




@bot.event
async def on_ready():
  print('Ready!')
  while True:
    await bot.change_presence(activity=discord.Streaming(name=f"=help | {len(bot.guilds)} 個伺服器", url="https://www.twitch.tv/kuan_owo_tw"))



@bot.command()
@commands.check(is_it_me)
async def load(ctx, extension):
  if extension == "all":
    embed=discord.Embed(title="Load", description=f"Load all", color=ctx.author.color)
    await ctx.send(embed=embed)
    for filename in os.listdir('./cmds'):
	    if filename.endswith('.py'):
		    bot.load_extension(f'cmds.{filename[:-3]}')
    return
  else:
    bot.load_extension(f'cmds.{extension}')
    embed=discord.Embed(title="Load", description=f"Load {extension}", color=ctx.author.color)
    await ctx.send(embed=embed)

@bot.command()
@commands.check(is_it_me)
async def unload(ctx, extension):
  if extension == "all":
    embed=discord.Embed(title="Unload", description=f"Unload all", color=ctx.author.color)
    await ctx.send(embed=embed)
    for filename in os.listdir('./cmds'):
	    if filename.endswith('.py'):
		    bot.unload_extension(f'cmds.{filename[:-3]}')
    return
  else:
    bot.unload_extension(f'cmds.{extension}')
    embed=discord.Embed(title="Unload", description=f"Unload {extension}", color=ctx.author.color)
    await ctx.send(embed=embed)

@bot.command()
@commands.check(is_it_me)
async def reload(ctx, extension):
  if extension == "all":
    embed=discord.Embed(title="Roload", description=f"Roload all", color=ctx.author.color)
    await ctx.send(embed=embed)
    for filename in os.listdir('./cmds'):
	    if filename.endswith('.py'):
		    bot.reload_extension(f'cmds.{filename[:-3]}')
    return
  else:
    bot.reload_extension(f'cmds.{extension}')
    embed=discord.Embed(title="Reload", description=f"Reload {extension}", color=ctx.author.color)
    await ctx.send(embed=embed)
    
@bot.command()
@commands.is_owner()
async def shutdown(ctx):
  await ctx.send("Shutting down...")
  await asyncio.sleep(1)
  await bot.logout()

for filename in os.listdir('./cmds'):
	if filename.endswith('.py'):
	  bot.load_extension(f'cmds.{filename[:-3]}')



if __name__ == "__main__":
  keep_alive.keep_alive()
  bot.run(token)
