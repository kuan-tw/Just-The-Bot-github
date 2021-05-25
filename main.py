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

load_dotenv()

token = os.getenv("DISCORD_BOT_SECRET")

intents = discord.Intents.all()

def is_it_me(ctx):
  return ctx.author.id == 536445172247167016 or 542715105276723202
  
bot = commands.Bot(command_prefix='=', intents=intents)
bot.remove_command('help')


@bot.event
async def on_ready():
    print('>Bot is ready<')
    while True:
      activity = discord.Game(f'=help | 獲得幫助')
      await bot.change_presence(status=discord.Status.online,activity=activity)
      await asyncio.sleep(5)
      activity2 = discord.Game(f'{len(bot.guilds)} 個伺服器') 
      await bot.change_presence(status=discord.Status.online, activity=activity2)
      await asyncio.sleep(5)
      activity3 = discord.Game(f'| 機器人版本 | v0.6 BETA |')
      await bot.change_presence(status=discord.Status.online,activity=activity3)
      await asyncio.sleep(5)

@bot.event
async def on_member_join(self, member):
  if str(member.guild.id) == "794519556881121320":
    channel = self.bot.get_channel(809986358638280734)
    channel1 = self.bot.get_channel(809986358638280734)
    embed = discord.Embed(title=f'歡迎{member.mention}加入', color=random.randint(0, 0xffffff))
    await channel1.send(embed=embed)

@bot.event
async def on_member_leave(self, member):
  if str(member.guild.id) == "794519556881121320":
    channel = self.bot.get_channel(809986358638280734)
    channel1 = self.bot.get_channel(809986358638280734)
    embed = discord.Embed(title=f'{member.mention}退出了', color=random.randint(0, 0xffffff))
    await channel1.send(embed=embed)


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
