import discord
from discord.ext import commands
import json
import asyncio
import datetime
import time
import random
import os

class Info(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def user(self, ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at, title=f"📶 用戶資訊 - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="🆔ID:", value=member.id)
    embed.add_field(name="ℹ️名字:", value=member.display_name)

    embed.add_field(name="📆帳戶創建時間:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="📆加入伺服器時間:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="📋身分組:", value="".join([role.mention for role in roles]))
    embed.add_field(name="📋最高身分組:", value=member.top_role.mention)
    print(member.top_role.mention)
    embed.set_footer(text='made by kuan 🇹🇼#6503')
    await ctx.send(embed=embed)

  @commands.command()
  async def server(self, ctx):
    all_member_num = len(ctx.guild.members)
    member_num = len(list(filter(lambda m: not m.bot, ctx.guild.members)))
    bot_num = len(list(filter(lambda m: m.bot, ctx.guild.members)))
    ge = 0
    e = 0
    for emoji in ctx.guild.emojis:
      if emoji.animated == True:
        ge += 1
      elif emoji.animated == False:
        e += 1
    online = 0
    idle = 0
    dnd = 0
    offline = 0
    for member in ctx.guild.members:
      if str(member.status) == "online":
        online += 1
      if str(member.status) == "idle":
        idle += 1
      if str(member.status) == "dnd":
        dnd += 1
      if str(member.status) == "offline":
        offline += 1
    text = 0
    news = 0
    category = 0
    store = 0
    voice = 0
    for channel in ctx.guild.channels:
      if str(channel.type) == "text":
        text += 1
      if str(channel.type) == "news":
        news += 1
      if str(channel.type) == "category":
        category += 1
      if str(channel.type) == "store":
        store += 1
      if str(channel.type) == "voice":
        voice += 1
    if str(ctx.guild.region) == "hongkong":
      region = ":flag_hk:HongKong"
    else:
      region = ctx.guild.region
    embed=discord.Embed(title='伺服器資訊',color=random.randint(150, 300))
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.add_field(name="📛名稱", value=f'{ctx.guild.name}', inline=True)  
    embed.add_field(name="🆔ID", value=f'{ctx.guild.id}', inline=True)  
    embed.add_field(name="👑擁有者", value=ctx.guild.owner.mention, inline=True)
    embed.add_field(name=f"👥總人數 - {all_member_num}", value=f"👤用戶 - {member_num}\n🤖機器人 - {bot_num}", inline=True) 
    embed.add_field(name="🌏伺服器位置", value=region, inline=True) 
    embed.add_field(name=":bar_chart:總身分組", value=f'{len(ctx.guild.roles)}', inline=True)      
    embed.add_field(name=f" 加成狀態", value=f'等級 - {int(ctx.guild.premium_tier)}\n次數 - {int(ctx.guild.premium_subscription_count)}', inline=True)
    embed.add_field(name=f"表情符號 - {len(ctx.guild.emojis)}", value=f'動態 - {ge}\n一般 - {e}', inline=True) 
    embed.add_field(name=f":file_folder:頻道數量 - {len(ctx.guild.channels)}", value=f":dividers:類別 - {category}\n:speech_balloon:文字 - {text}\n:loud_sound:語音 - {voice}\n📢公告 - {news}\n🔖商店 - {store}")
    embed.add_field(name=f"用戶狀態 - {len(ctx.guild.members)}", value=f"線上 - {online}\n閒置 - {idle}\n請勿打擾 - {dnd}\n隱形/離線 - {offline}") 
    embed.add_field(name="🕒 伺服器創建於 (UTC)", value=f'{ctx.guild.created_at.__format__("%A/%d/%B/%Y  %H:%M:%S")}', inline=True)
    embed.set_footer(text='made by kuan 🇹🇼#6503')
    await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(Info(bot))