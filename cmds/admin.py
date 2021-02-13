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
  @commands.has_permissions(administrator=True)
  async def anno(self, ctx, *,msg):
    await ctx.message.delete()
    embed=discord.Embed(title='公告', color=random.randint(0, 0xffffff))
    embed.add_field(name='訊息', value=msg)
    await ctx.send("||@everyone||", embed=embed)
  
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def guild(self, ctx):
    guildlist = []
    for list in self.bot.guilds:
      nameid = f"{list.name}({list.id}[{list.owner}])"
      guildlist.append(nameid)
    guild = "\n\n".join(guildlist)
    await ctx.send(f"```{guild}```")

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def kick(self, ctx, member:discord.Member=None, *, reason=None):
    embed=discord.Embed(title="**指令錯誤**", description="你不能踢出你自己", colour=random.randint(0, 0xffffff))
    embed2=discord.Embed(title="**指令錯誤**", description="請輸入一位成員\n**用法**\nc!kick @Member/ID <reason>", colour=random.randint(0, 0xffffff))
    if member is None:
        await ctx.send(embed=embed2)
    elif member is ctx.author:
        await ctx.send(embed=embed)
        return
    else:
        embedTW3=discord.Embed(title=f"踢出", color=0xbcff7d , timestamp =datetime.datetime.utcnow())
        embedTW3.set_author(name=member, icon_url=member.avatar_url)
        embedTW3.add_field(name="原因", value=f"{reason}", inline=False)
        embedTW3.add_field(name="執行者", value=f"{ctx.author.name}#{ctx.author.discriminator}", inline=False)
        embedTW3.set_footer(text="kuan 🇹🇼#6503|coal|XiaYue#0898技術支援")
        await ctx.send(embed=embedTW3)
        await member.kick(reason=reason)
        user = self.bot.get_user(member.id)
        await user.send(embed=embedTW3)

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def ban(self, ctx, member:discord.Member=None, *, reason=None):
    embedTW1=discord.Embed(title="**指令錯誤**", description="你不能封鎖你自己", colour=random.randint(0, 0xffffff))
    embedTW4=discord.Embed(title="**指令錯誤**", description="請輸入一位成員\n**用法**\nc!ban @Member/ID <reason>", colour=random.randint(0, 0xffffff))
    if member is None:
        await ctx.send(embed=embedTW4)
        return
    elif member is ctx.author:
        await ctx.send(embed=embedTW1)
        return
    else:
        embedTW3=discord.Embed(title=f"封鎖", color=0xbcff7d , timestamp =datetime.datetime.utcnow())
        embedTW3.set_author(name=member, icon_url=member.avatar_url)
        embedTW3.add_field(name="原因", value=f"{reason}", inline=False)
        embedTW3.set_footer(text="kuan 🇹🇼#6503|coal|XiaYue#0898技術支援")
        embedTW3.add_field(name="執行者", value=f"{ctx.author.name}#{ctx.author.discriminator}", inline=False)
        await ctx.send(embed=embedTW3)
        await member.ban(reason=reason)
        user = self.bot.get_user(member.id)
        await user.send(embed=embedTW3)

  

  


def setup(bot):
  bot.add_cog(Admin(bot))