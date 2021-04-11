import discord
from discord.ext import commands
import json
import asyncio
import datetime
import time
import random
import os


class Help(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def help(self, ctx):
    embed = discord.Embed(title='指令列表', description='prefix`=`', color=random.randint(0, 0xffffff))
    embed.add_field(name='⚒️主要指令', value='`ping` `inv` `say` `thinking` `random`', inline=True)
    embed.add_field(name='🖥️資訊類', value='`user` `server` `channel` `bot` `avatar`', inline=True)
    embed.add_field(name='⚙️管理員指令', value='`anno` `clean` `kick` `ban`', inline=True)
    embed.add_field(name='💡幫助類', value='`main` `info` `admin` `fun` `game` `gobal` `math`')
    embed.add_field(name='📺娛樂', value='`dice` `gay` `question` `num` `sayc` `meme`')
    embed.add_field(name='🔬數學', value='`plus` `minus` `times` `into` `areseq`')
    embed.add_field(name='🕹️遊戲類', value='`skull` `skin` `mcserver`', inline=True)
    embed.add_field(name='🦠國際', value='`corona` `weather`')
    embed.add_field(name='<:hypixel:830389994384130068>Hypixel', value='`hyp` `bw`')
    embed.set_footer(text='made by kuan 🇹🇼#6503')
    await ctx.send(embed=embed)
  
  @commands.command()
  async def main(self, ctx):
    embed = discord.Embed(title='指令列表-主要指令',color=random.randint(50,300))
    embed.add_field(name='ping', value='顯示機器人延遲')
    embed.add_field(name='inv', value='邀請連結')
    embed.add_field(name='say', value='覆誦訊息')
    embed.add_field(name='thinking', value='思考')
    embed.add_field(name='random <數字>', value='從0到你輸入的數字隨機取數')
    embed.set_footer(text='made by kuan 🇹🇼#6503')
    await ctx.send(embed=embed)
  
  @commands.command()
  async def info(self, ctx):
    embed = discord.Embed(title='指令列表-資訊類',color=random.randint(50,300))
    embed.add_field(name='server', value='伺服器資訊')
    embed.add_field(name='user', value='用戶資訊')
    embed.add_field(name='channel', value='頻道資訊')
    embed.add_field(name='bot', value='機器人資訊')
    embed.add_field(name='avatar', value='查看頭像')
    embed.set_footer(text='made by kuan 🇹🇼#6503')
    await ctx.send(embed=embed)

  @commands.command()
  async def admin(self, ctx):
    embed = discord.Embed(title='指令列表-管理員指令',color=random.randint(50,300))
    embed.add_field(name='anno', value='公告')
    embed.add_field(name='clean', value='清理訊息')
    embed.add_field(name='kick <成員>', value='踢出成員')
    embed.add_field(name='ban <成員>', value='封鎖成員')
    embed.set_footer(text='made by kuan 🇹🇼#6503')
    await ctx.send(embed=embed)

  @commands.command()
  async def fun(self, ctx):
    embed = discord.Embed(title='指令列表-娛樂', color=random.randint(0, 0xffffff))
    embed.add_field(name='dice', value='骰子')
    embed.add_field(name='gay', value='偵測gay的機率')
    embed.add_field(name='question', value='問問題')
    embed.add_field(name='num <起始數字> <次數>', value='數數字')
    embed.add_field(name='sayc <次數> <訊息>', value='刷屏功能')
    embed.add_field(name='meme', value='隨機迷因')
    await ctx.send(embed=embed)

  @commands.command()
  async def game(self, ctx):
    embed = discord.Embed(title='指令列表-遊戲', color=random.randint(0, 0xffffff))
    embed.add_field(name='skull <MCID>', value='生成minecraft頭顱指令', inline=True)
    embed.add_field(name='skin <MCID>', value='查詢玩家skin', inline=True)
    embed.add_field(name='mcserver <ip>', value='查詢伺服器資訊', inline=True)
    await ctx.send(embed=embed)

  @commands.command()
  async def gobal(self, ctx):
    embed = discord.Embed(title='指令列表-國際', color=random.randint(0, 0xffffff))
    embed.add_field(name='corona <國家>(若要查看全球國家打world)', value='查看某國疫情', inline=True)
    embed.add_field(name='weather <城市>', value='查看某城市的天氣')
    await ctx.send(embed=embed)

  @commands.command()
  async def math(self, ctx):
    embed= discord.Embed(title='指令列表-數學', color=random.randint(0, 0xffffff))
    embed.add_field(name='plus <數字> <數字>', value='加法')
    embed.add_field(name='minus <數字> <數字>', value='減法')
    embed.add_field(name='times <數字> <數字>', value='乘法')
    embed.add_field(name='into <數字> <數字>', value='除法')
    embed.add_field(name='areseq <第1項> <欲查看的項數> <公差>', value='等差數列')
    await ctx.send(embed=embed)


    
    


def setup(bot):
  bot.add_cog(Help(bot))