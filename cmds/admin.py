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
    embed=discord.Embed(title='公告', description=msg, color=random.randint(0, 0xffffff))
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
        embedTW3.set_footer(text="kuanTW#6503|coal|XiaYue#0898技術支援")
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
        embedTW3.set_footer(text="kuanTW#6503|coal|XiaYue#0898技術支援")
        embedTW3.add_field(name="執行者", value=f"{ctx.author.name}#{ctx.author.discriminator}", inline=False)
        await ctx.send(embed=embedTW3)
        await member.ban(reason=reason)
        user = self.bot.get_user(member.id)
        await user.send(embed=embedTW3)

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def mute(self, ctx, member:discord.Member=None,*, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")
    mem = discord.utils.get(guild.roles, name='國民')

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title="muted", description=f"{member.mention} was muted ", colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.remove_roles(mem)
    await member.send(f" you have been muted from: {guild.name} reason: {reason}")
  
    
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def unmute(self, ctx, member: discord.Member):
   guild = ctx.guild
   mutedRole = discord.utils.get(guild.roles, name="Muted")
   mem = discord.utils.get(guild.roles, name='國民')

   await member.remove_roles(mutedRole)
   await member.add_roles(mem)
   await member.send(f" you have unmutedd from: - {ctx.guild.name}")
   embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=discord.Colour.light_gray())
   await ctx.send(embed=embed)

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def vote(self, ctx, item=None, titem=None, ritem=None, fitem=None):
    if item is None:
      await ctx.send(embed=discord.Embed(title='請輸入2個選項', color=random.randint(0, 0xffffff)))
    elif titem is None:
      await ctx.send(embed=discord.Embed(title='請輸入2個選項', color=random.randint(0, 0xffffff)))
    else: 
      if item is not None:
        if titem is not None:
          if ritem is None:
            embed = discord.Embed(title='投票', color=random.randint(0, 0xffffff))
            embed.add_field(name=f'-1️⃣-', value=f'{item}')
            embed.add_field(name=f'-2️⃣-', value=f'{titem}')
            message = await ctx.send(embed=embed)
            await message.add_reaction('1️⃣')
            await message.add_reaction('2️⃣')
    
    if ritem is not None:
      if fitem is None:
        rembed = discord.Embed(title='投票', color=random.randint(0, 0xffffff))
        rembed.add_field(name=f'-1️⃣-', value=f'{item}')
        rembed.add_field(name=f'-2️⃣-', value=f'{titem}')
        rembed.add_field(name=f'-3️⃣-', value=f'{ritem}')
        rmessage = await ctx.send(embed=rembed)
        await rmessage.add_reaction('1️⃣')
        await rmessage.add_reaction('2️⃣')
        await rmessage.add_reaction('3️⃣')

    if ritem is not None:
      if fitem is not None:
        fembed = discord.Embed(title='投票', color=random.randint(0, 0xffffff))
        fembed.add_field(name=f'-1️⃣-', value=f'{item}')
        fembed.add_field(name=f'-2️⃣-', value=f'{titem}')
        fembed.add_field(name=f'-3️⃣-', value=f'{ritem}')
        fembed.add_field(name=f'-4️⃣-', value=f'{fitem}')
        fmessage = await ctx.send(embed=fembed)
        await fmessage.add_reaction('1️⃣')
        await fmessage.add_reaction('2️⃣')
        await fmessage.add_reaction('3️⃣')
        await fmessage.add_reaction('4️⃣')

    


    
    


  

  


def setup(bot):
  bot.add_cog(Admin(bot))