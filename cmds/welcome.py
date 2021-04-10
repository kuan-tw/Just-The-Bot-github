import discord
from discord.ext import commands
import json
import asyncio
import datetime
import time
import random
import os

class Welcome(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_member_join(self, member):
    if str(member.guild.id) == "794519556881121320":
      channel = self.bot.get_channel(809986358638280734)
      channel1 = self.bot.get_channel(809986358638280734)
      embed = discord.Embed(title=f'歡迎{member.mention}加入', color=random.randint(0, 0xffffff))
      await channel1.send(embed=embed)

  @commands.Cog.listener()
  async def on_member_leave(self, member):
    if str(member.guild.id) == "794519556881121320":
      channel = self.bot.get_channel(809986358638280734)
      channel1 = self.bot.get_channel(809986358638280734)
      embed = discord.Embed(title=f'{member.mention}退出了', color=random.randint(0, 0xffffff))
      await channel1.send(embed=embed)

    

def setup(bot):
  bot.add_cog(Welcome(bot))