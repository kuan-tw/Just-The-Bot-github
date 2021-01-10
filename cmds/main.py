import discord
from discord.ext import commands
import json
import asyncio
import datetime
import time
import random
import os
import math

class Main(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def ping(self, ctx):
    embed=discord.Embed(title='機器人延遲', color=random.randint(1, 350)) 
    embed.add_field(name='延遲(ms)', value=round(self.bot.latency*1000))
    await ctx.send(embed=embed)

  @commands.command()
  async def thinking(self, ctx):
    user_name = ctx.message.author.mention
    await ctx.send(f'{user_name}  :thinking:')

  @commands.command()
  async def inv(self, ctx):
    embed=discord.Embed(title='邀請連結', url='https://reurl.cc/pyXd9Q')
    embed.set_footer(text='made by kuan 🇹🇼#6503')
    await ctx.send(embed=embed)

  @commands.command()
  async def say(self, ctx, *,msg):
    await ctx.message.delete()
    await ctx.send(msg)




def setup(bot):
  bot.add_cog(Main(bot))