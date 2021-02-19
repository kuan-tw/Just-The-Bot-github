import discord
from discord.ext import commands
import json
import asyncio
import datetime
import time
import os
import math
import random

class Math(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def plus(self, ctx, a:int, b:int):
    c = a + b
    embed = discord.Embed(title='加法', description=f'{a} + {b} = {c}', color=random.randint(0, 0xffffff))
    await ctx.send(embed=embed)

  @commands.command()
  async def minus(self, ctx, a:int, b:int):
    c = a - b
    embed = discord.Embed(title='減法', description=f'{a} - {b} = {c}', color=random.randint(0, 0xffffff))
    await ctx.send(embed=embed)

  @commands.command()
  async def times(self, ctx, a:int, b:int):
    c = a * b
    embed = discord.Embed(title='乘法', description=f'{a} x {b} = {c}', color=random.randint(0, 0xffffff))
    await ctx.send(embed=embed)

  @commands.command()
  async def into(self, ctx, a:int, b:int):
    c = a / b
    embed = discord.Embed(title='除法', description=f'{a} ÷ {b} = {c}', color=random.randint(0, 0xffffff))
    await ctx.send(embed=embed)




def setup(bot):
  bot.add_cog(Math(bot))