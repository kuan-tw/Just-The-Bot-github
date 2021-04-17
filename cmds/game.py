import discord
from discord.ext import commands
import json
import asyncio
import datetime
import time
import os
import math
import random
import io
import requests

API_KEY = '092f48b3-ea7c-43b8-87b9-b225836ee963'

ranks = {"VIP":"[VIP]","VIP_PLUS":"[VIP+]","MVP":"[MVP]","MVP_PLUS":"[MVP+]","SUPERSTAR":"[MVP++]","YOUTUBER":"[YOUTUBE]","ADMIN":"[ADMIN]"}

class Game(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command()
  async def skull(self, ctx, *,msg=None):
    if msg == None:
      await ctx.send(embed=discord.Embed(description=f":x: | 請輸入一個玩家",color=discord.Color.red()))
      return
    username = msg
    url = f'https://api.mojang.com/users/profiles/minecraft/{username}?'
    response = requests.get(url)
    try:
      uuid = response.json()['id']
    except:
      await ctx.send(embed=discord.Embed(description=f":x: | 找不到 **{msg}** 這個玩家",color=discord.Color.red()))
      return
    embed = discord.Embed(title="minecraft 頭顱生成器", description="生成指令如下", colour=random.randint(0, 0xffffff))
    embed.set_thumbnail(url=f"https://crafatar.com/avatars/{uuid}")
    embed.add_field(name="ID", value=msg, inline=True)
    embed.add_field(name="1.12-", value='`/give @p minecraft:skull 1 3 ' + '{SkullOwner:' + f'"{msg}" ' + '}`', inline=True)
    embed.add_field(name='1.13+', value='`/give @p minecraft:player_head' + '{SkullOwner:' + f'"{msg}"'+'}`')
    await ctx.send(embed=embed)

  @commands.command()
  async def skin(self, ctx, *,msg=None):
    if msg == None:
      await ctx.send(embed=discord.Embed(description=f":x: | 請輸入一個玩家",color=discord.Color.red()))
      return
    username = msg
    url = f'https://api.mojang.com/users/profiles/minecraft/{username}?'
    response = requests.get(url)
    try:
      uuid = response.json()['id']
    except:
      await ctx.send(embed=discord.Embed(description=f":x: | 找不到 **{msg}** 這個玩家",color=discord.Color.red()))
      return
    embed = discord.Embed(title='minecraft skin 查詢', description='結果如下', colour=random.randint(0, 0xffffff))
    embed.set_image(url=f"https://crafatar.com/renders/body/{uuid}")
    await ctx.send(embed=embed)

  @commands.command()
  async def mcserver(self, ctx, *,msg=None):
    if msg == None:
      await ctx.send(embed=discord.Embed(description=f":x: | 請輸入一個伺服器",color=discord.Color.red()))
      return
    address = msg
    url = f'https://api.mcsrvstat.us/2/{address}'
    response = requests.get(url)
    x = response.json()
    ip = x['ip']
    port = x['port']
    try:
      host = x['hostname']
    except:
      await ctx.send(embed=discord.Embed(description=f":x: | 找不到 **{msg}** 這個伺服器",color=discord.Color.red()))
      return
    ver = x['version']
    icon = f'https://api.mcsrvstat.us/icon/{address}'
    m = x['motd']
    motd = m['clean']
    p = x['players']
    online = p['online']
    maxplayer = p['max']
    embed = discord.Embed(title='minecraft伺服器資訊', description=f'伺服器:{address}', colour=random.randint(0, 0xffffff))
    embed.set_thumbnail(url=icon)
    embed.add_field(name='ip', value=ip, inline=True)
    embed.add_field(name='port', value=port, inline=True)
    embed.add_field(name='motd', value=f'`motd`', inline=True)
    embed.add_field(name='版本', value=ver, inline=True)
    embed.add_field(name='線上玩家', value=online, inline=True)
    embed.add_field(name='最多可容納玩家', value=maxplayer, inline=True)
    embed.add_field(name='host', value=host, inline=True)
    await ctx.send(embed=embed)


def setup(bot):
  bot.add_cog(Game(bot))