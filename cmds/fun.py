import discord
from discord.ext import commands
import json
import asyncio
import datetime
import time
import os
import math
import random
from pyrandmeme import *

answer = [ "是✔","不是❌","我不知道😔","可能:thinking:"]
a = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0"]
ate = ["還不錯", "噁", "根廚餘沒兩樣", "好吃!", "我要吐了"]
ns = ["大便", "屎", "shit", "poo"]

class Fun(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  

  # @commands.Cog.listener()
  # async def on_message(self, message):
  #   msg = message.content
  #   if "northkorea" in msg.lower():
  #     if message.author.bot:
  #       return
  #     await message.channel.send("<:NorthKorea:799237129011593226>")
  #   elif "usa" in msg.lower():
  #     if message.author.bot:
  #       return
  #     await message.channel.send("<:USA:799229250460712981>")
  #   elif "ussr" in msg.lower():
  #     if message.author.bot:
  #       return
  #     await message.channel.send("<:USSR:799230151815987200>")
  #   elif "qing" in msg.lower():
  #     if message.author.bot:
  #       return
  #     await message.channel.send("<:Qing:799233451626725376>")

  
  @commands.command()
  async def dice(self, ctx):
    rand = random.randint(1, 6)
    user_name = ctx.message.author.mention
    await ctx.send(f':game_die:{user_name}骰到了{rand}:game_die:')

  @commands.command()
  async def gay(self, ctx, *, member:discord.Member=None, tag=''):
    member = ctx.author if not member else member
    num = random.randrange(1, 101)
    embed = discord.Embed(title="", description=f"**👬 {member.name} 有 {num}% 是 GAY 👬**", colour=random.randint(0, 0xffffff))
    await ctx.send(embed=embed)

  @commands.command() 
  async def question(self, ctx , *, question=None):
    if question is None:
      embed=discord.Embed(title="**指令錯誤**", description="請輸入正確的問題\n**用法**\n=question <question>", colour=random.randint(0, 0xffffff))
    else:
      embed=discord.Embed(title="", description="", colour=random.randint(0, 0xffffff))
      embed.add_field(name="問題", value=question, inline=True)
      embed.add_field(name="答案", value=random.choice(answer), inline=True)
    await ctx.send(embed=embed)
  
  @commands.command()
  async def num(self, ctx, num:int, i:int):
    for i in range(i):
      await ctx.send(num+1)
      num += 1
    await ctx.send("數數字完成")

  @commands.command()
  async def meme(self, ctx):
    await ctx.send(embed=await pyrandmeme())

  @commands.command()
  async def sayc(self, ctx, num:int, *,msg):
    await ctx.message.delete()
    for num in range(num):
      await ctx.send(msg)
  
  @commands.command()
  async def nitro(self, ctx):
    ns = []
    l = []
    for x in range(16):
      l.append(random.choice(a))
    link = "".join(l)
    await ctx.send(f"https://discord.gift/{link}")

  @commands.command()
  async def eat(self, ctx, food=None):
    if food is None:
      await ctx.send('阿你沒東西我要怎麼吃')
    elif food.lower() in ns :
      await ctx.send('你才吃屎 你全家都吃屎')
    else:
      embed=discord.Embed(title="", description="", colour=random.randint(0, 0xffffff))
      embed.add_field(name="食物", value=food, inline=True)
      embed.add_field(name="品嘗過後的心得", value=random.choice(ate), inline=True)
      await ctx.send(embed=embed)





def setup(bot):
  bot.add_cog(Fun(bot))