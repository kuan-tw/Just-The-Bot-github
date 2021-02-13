import discord
from discord.ext import commands
import json
import asyncio
import datetime
import time
import random
import os
import math
from urllib import parse, request
import re

class Main(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def ping(self, ctx):
    embed=discord.Embed(title='機器人延遲(ms)', description=round(self.bot.latency*1000), color=random.randint(0, 0xffffff)) 
    await ctx.send(embed=embed)

  @commands.command()
  async def thinking(self, ctx):
    user_name = ctx.message.author.mention
    await ctx.send(f'{user_name}  :thinking:<:RealChina:795218598285148160>') 

  @commands.command()
  async def inv(self, ctx):
    embed=discord.Embed(title='邀請連結', url='https://reurl.cc/pyXd9Q')
    embed.set_footer(text='made by kuan 🇹🇼#6503')
    await ctx.send(embed=embed)
  
  @commands.command()
  async def eula(self, ctx):
    embed=discord.Embed(title='機器人條款', color=random.randint(0, 0xffffff))
    embed.add_field(name='第一', value='本機器人只承認:flag_tw:中華民國 去你的共匪~~flag_cn~~')
    embed.add_field(name='第二', value='反共復國 拯救同胞')
    embed.add_field(name='第三', value='殺朱拔毛 反共抗俄')
    embed.add_field(name='第四', value='消滅朱毛漢賊 解救大陸同胞')
    embed.add_field(name='第五', value='三民主義 統一中國')
    embed.add_field(name='第六', value='軍人之恥 共匪不滅')
    embed.add_field(name='第七', value='全力支援前線 準備反攻大陸')
    embed.add_field(name='第八', value='一年準備、二年反攻、三年掃蕩、五年成功')
    embed.set_footer(text='made by Republic of China')
    await ctx.send(embed=embed)

  @commands.command()
  async def say(self, ctx, *,msg):
    await ctx.message.delete()
    await ctx.send(msg)

  @commands.command(pass_context=True)
  async def random(self, ctx, *,number):
    try:
        arg = random.randint(1, int(number))
    except ValueError:
        await ctx.send("Invalid number")
    else:
        await ctx.send(str(arg))

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def clean(self, ctx, num:int):
    await ctx.channel.purge(limit=num+1)
    await ctx.send(f'清理{num+1}則訊息(此訊息會自動刪除)')
    await asyncio.sleep(5)
    await ctx.channel.purge(limit=1)

  @commands.command()
  async def google(self, ctx, *,msg):
    url = f'https://www.google.com/search?q={msg}'
    embed = discord.Embed(title=f'{msg}', url=url)
    await ctx.send(embed=embed)


  @commands.Cog.listener()
  async def on_message(self, message):
    msg = message.content
    if "china" in msg.lower():
      if message.author.bot:
        return
      await message.channel.send("<:RealChina:795218598285148160>")




def setup(bot):
  bot.add_cog(Main(bot))