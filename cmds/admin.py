import discord
from discord.ext import commands
import json
import asyncio
import datetime
import time
import random
import os

class Admin(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def anno(self, ctx, *,msg):
    await ctx.message.delete()
    embed=discord.Embed(title='公告', color=random.randint(1, 255))
    embed.add_field(name='訊息', value=msg)
    await ctx.send("||@everyone||", embed=embed)


def setup(bot):
  bot.add_cog(Admin(bot))