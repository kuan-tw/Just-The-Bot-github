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

  def cog_unload(self):
    self.slash.remove_cog_commands(self)
    pass

  @commands.command()
  async def help(self, ctx, *, msg=None):
    if msg is None :
      embed = discord.Embed(title='幫助', color=random.randint(0, 0xffffff))
      embed.add_field(name='Hi 我叫Just The Bot\n若需要幫助請輸入`=help commands`\n有任何問題請加入官方支援群\n若想查看單獨的指令列表\n 可在`=help`後輸入以下參數\n`main info admin fun game gobal math hypixel`', value='🛠️[官方支援群](https://discord.gg/utpxQN4U5M) \n▶️[邀請機器人](https://discord.com/oauth2/authorize?client_id=772285245923917862&permissions=0&scope=bot%20applications.commands)\n💻[官方網站(Beta)](https://just-the-bot.netlify.app/)\n⭐[贊助我](https://paypal.me/kuantw)')
      embed.set_footer(text='kuan 🇹🇼#6503版權所有\n kuan 🇹🇼#6503© 2020, 2021')
      await ctx.send(embed=embed)
    if msg is not None:
      if msg == "commands":
        c = discord.Embed(title='指令列表', description='prefix `=`\n <>表示必選\n[]表示可選', color=random.randint(0, 0xffffff))
        c.add_field(name='⚒️主要指令', value='`ping` `inv` `say` `thinking` `random`', inline=True)
        c.add_field(name='🖥️資訊類', value='`user` `server` `channel` `bot` `avatar`', inline=True)
        c.add_field(name='⚙️管理員指令', value='`anno` `clean` `kick` `ban` `vote`', inline=True)
        c.add_field(name='📺娛樂', value='`dice` `gay` `question` `num` `sayc` `meme` `eat`')
        c.add_field(name='🔬數學', value='`plus` `minus` `times` `into` `areseq`')
        c.add_field(name='🕹️遊戲類', value='`skull` `skin` `mcserver`', inline=True)
        c.add_field(name='🦠國際', value='`corona` `weather` `eq` `twrain`')
        c.add_field(name='<:hypixel:830389994384130068>Hypixel', value='`hyp` `bw` `hypimg`')
        c.set_footer(text='made by kuan 🇹🇼#6503')
        await ctx.send(embed=c)
      elif msg == "main":
        m = discord.Embed(title='指令列表-主要指令',color=random.randint(50,300))
        m.add_field(name='ping', value='顯示機器人延遲')
        m.add_field(name='inv', value='邀請連結')
        m.add_field(name='say', value='覆誦訊息')
        m.add_field(name='thinking', value='思考')
        m.add_field(name='random <數字>', value='從0到你輸入的數字隨機取數')
        m.set_footer(text='made by kuan 🇹🇼#6503')
        await ctx.send(embed=m)
      elif msg == "info":
        i = discord.Embed(title='指令列表-資訊類',color=random.randint(50,300))
        i.add_field(name='server', value='伺服器資訊')
        i.add_field(name='user', value='用戶資訊')
        i.add_field(name='channel', value='頻道資訊')
        i.add_field(name='bot', value='機器人資訊')
        i.add_field(name='avatar', value='查看頭像')
        i.set_footer(text='made by kuan 🇹🇼#6503')
        await ctx.send(embed=i)
      elif msg == "admin":
        a = discord.Embed(title='指令列表-管理員指令',color=random.randint(50,300))
        a.add_field(name='anno', value='公告')
        a.add_field(name='clean', value='清理訊息')
        a.add_field(name='kick <成員> [原因]', value='踢出成員')
        a.add_field(name='ban <成員> [原因]', value='封鎖成員')
        a.add_field(name='vote <選項> <選項> [選項] [選項] ', value='投票')
        a.set_footer(text='made by kuan 🇹🇼#6503')
        await ctx.send(embed=a)
      elif msg == "fun":
        f = discord.Embed(title='指令列表-娛樂', color=random.randint(0, 0xffffff))
        f.add_field(name='dice', value='骰子')
        f.add_field(name='gay', value='偵測gay的機率')
        f.add_field(name='question', value='問問題')
        f.add_field(name='num <起始數字> <次數>', value='數數字')
        f.add_field(name='sayc <次數> <訊息>', value='刷屏功能')
        f.add_field(name='meme', value='隨機迷因')
        f.add_field(name='eat <食物>', value='吃東西')
        
        await ctx.send(embed=f)
      elif msg == "game":
        g = discord.Embed(title='指令列表-遊戲', color=random.randint(0, 0xffffff))
        g.add_field(name='skull <MCID>', value='生成minecraft頭顱指令', inline=True)
        g.add_field(name='skin <MCID>', value='查詢玩家skin', inline=True)
        g.add_field(name='mcserver <ip>', value='查詢伺服器資訊', inline=True)
        await ctx.send(embed=g)
      elif msg == "gobal":
        w = discord.Embed(title='指令列表-國際', color=random.randint(0, 0xffffff))
        w.add_field(name='corona [國家]', value='查看某國疫情', inline=True)
        w.add_field(name='weather <城市>', value='查看某城市的天氣')
        w.add_field(name='eq', value='地震報告')
        w.add_field(name='twrain <測站ID> <月份>', value='[測站ID列表請點我](https://e-service.cwb.gov.tw/wdps/obs/state.htm)\n **列表中的測站不一定全部都可查詢**')
        await ctx.send(embed=w)
      elif msg == "math":
        m = discord.Embed(title='指令列表-數學', color=random.randint(0, 0xffffff))
        m.add_field(name='plus <數字> <數字>', value='加法')
        m.add_field(name='minus <數字> <數字>', value='減法')
        m.add_field(name='times <數字> <數字>', value='乘法')
        m.add_field(name='into <數字> <數字>', value='除法')
        m.add_field(name='areseq <第1項> <欲查看的項數> <公差>', value='等差數列')
        await ctx.send(embed=embed)
      elif msg == "hypixel":
        h = discord.Embed(title='指令列表-Hypixel', color=random.randint(0, 0xffffff))
        h.add_field(name='hyp <MCID>', value='Hypixel玩家資訊')
        h.add_field(name='bw <MCID>', value='Hypixel床戰玩家資訊')
        h.add_field(name='hypimg <MCID>', value='Hypixel玩家資訊圖片版')
        await ctx.send(embed=h)
      else:
        error=discord.Embed(title=':x: | 未知的參數', color=discord.Color.red())
        await ctx.send(embed=error)








    
    


def setup(bot):
  bot.add_cog(Help(bot))