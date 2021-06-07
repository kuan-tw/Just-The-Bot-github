import discord
from discord.ext import commands
import json
import asyncio
import datetime
import time
import os
import math
import random
import io
import requests

ranks = {"VIP":"<:VIP1:849149582675148823><:VIP2:849149665844920330><:VIP3:849149715769065472>","VIP_PLUS":"<:VIP1p:849162779118403615><:VIP2p:849162636959678504><:VIP3p:849162164627177553>","MVP":"<:MVP1:849163934434590720><:MVP2:849164000885342239><:MVP3:849164044732858368>","MVP_PLUS":f"<:mvp_plus1:849952191951011870><:mvp_plus2:849952252269035521><:mvp_plus3:849952501280014396><:plus_red:850266057989423135>","SUPERSTAR":"[MVP++]","YOUTUBER":"<:yt1:849165730931146773><:yt2:849165834160832520><:yt3:849165878787833857><:yt4:849165926141526017><:yt5:849165958278938645>","ADMIN":"<:admin1:849179000940265492><:admin2:849179041550041119><:admin3:849179078467911680><:admin4:849179126095282180>"}
rankpluscolor = {"BLACK": "<:mvp_plus1:849952191951011870><:mvp_plus2:849952252269035521><:mvp_plus3:849952501280014396><:plus_black:849952545278525451>"}





class Hyp(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(description="查看玩家狀態或是Hypixel資料",usage="=hyp [玩家名]")
  async def hyp(self, ctx, name=None):
        message = await ctx.send(embed=discord.Embed(
            description="<a:loading:830383608463228948> | 查詢中 請稍後",color=discord.Color.green()))
        try:
            data = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{name}").json()
        except:
            await message.edit(embed=discord.Embed(description=f":x: | 找不到 **{name}** 這個玩家",color=discord.Color.red()))
            return
        mc = requests.get(f"https://api.hypixel.net/player?key=092f48b3-ea7c-43b8-87b9-b225836ee963&uuid={data['id']}").json()
        p = mc["player"]
        if str(p) == "None":
            embed = discord.Embed(title="Minecraft 玩家狀態",colour=random.randint(0, 0xffffff))
            embed.add_field(name= "Name",value=name)
            embed.add_field(name= "UUID",value=data["id"])
            embed.set_thumbnail(url=f"https://crafatar.com/renders/body/{data['id']}")
            await message.edit(embed= embed)
            return
        else:
            if "prefix" in p:
                r = "<:owner1:849196627642155028><:owner2:849196670796562442><:owner3:849196722827558943><:owner4:849196873817784351>"
            else:
                if "rank" in p:
                    if str(p["rank"]) in ranks:
                        r = ranks[p["rank"]]
                    else:
                        r = p["rank"]
                else:
                    if "mostRecentMonthlyPackageRank" in p:
                        if str(p["mostRecentMonthlyPackageRank"]) in ranks:
                            r = ranks[p["mostRecentMonthlyPackageRank"]]
                        else:
                            r = p["mostRecentMonthlyPackageRank"]
                    else:
                        if "newPackageRank" in p:
                            if str(p["newPackageRank"]) in ranks:
                                r = ranks[p["newPackageRank"]]
                        else:
                            r = ""               
            if "networkExp" not in p:
                network_level = 0
            else:
                exp = p["networkExp"]
                network_level = (math.sqrt((2 * exp) + 30625) / 50) - 2.5
                network_level = round(network_level, 2)
            if "karma" in p:
                k = p["karma"]
            else:
                k = 0
            if "firstLogin" not in p:
                fl = "不可考"
            else:
                f = p["firstLogin"]/1000
                fll = f + 28800
                fl = datetime.datetime.fromtimestamp(int(fll)).strftime('%Y年%m月%d日 %H:%M:%S')
            if "lastLogin" not in p:
                t = "不可考"
            else:
                l = p["lastLogin"]/1000
                lll = l + 28800
                n = time.time()
                no = n + 28800
                work_seconds = int(no - lll)
                if work_seconds >= 60:
                    work_minutes = int((no - lll)/(60))
                    if work_minutes >= 60:
                        work_hours = int((no - lll)/(60*60))
                        if work_hours >= 24:
                            work_days= int((no - lll)/(24*60*60))
                            t = f"{work_days}天前"
                        else:
                            t = f"{work_hours}小時前"
                    else:
                        t = f"{work_minutes}分鐘前"
                else:
                    t = f"{work_seconds} 秒前"
            if name == "Technoblade":
              r = "<:pig1:849180613419991070><:pig2:849180648426045500><:pig3:849180680104968192><:pig4:849180713316253696>"
            if name == "HypixelEvents":
              r = "<:ev1:850715152944332842><:ev2:850715222225584159><:ev3:850715281491230740><:ev4:850715317066792970>"
            if str(r) == "NORMAL":
                r = ""
            if 'monthlyPackageRank' in p:
              mr = p['monthlyPackageRank']
              if "prefix" not in p:
                if mr == "NONE":
                  color = p['rankPlusColor']
                  embcolor = "<:plus_red:850266057989423135>"
                  if color == "BLACK":
                    embcolor = "<:plus_black:849952545278525451>"
                  elif color == "GOLD":
                    embcolor = "<:plus_orange:850220961868677170>"
                  elif color == "YELLOW":
                    embcolor = "<:plus_yellow:850229249687814165>"
                  elif color == "DARK_GRAY":
                    embcolor = "<:plus_gray:850230430166941736>"
                  elif color == "DARK_PURPLE":
                    embcolor = "<:plus_purple:850399455048237057>"
                  elif color == "GREEN":
                    embcolor = "<:plus_green:850304607505743883>"
                  r = f"<:mvp_plus1:849952191951011870><:mvp_plus2:849952252269035521><:mvp_plus3:849952501280014396>{embcolor}"
            embed1 = discord.Embed(title=f"{r}{p['displayname']}",colour=random.randint(0, 0xffffff))
            embed1.set_thumbnail(url=f"https://crafatar.com/renders/body/{data['id']}")
            embed1.add_field(name="UUID",value=data["id"])
            embed1.add_field(name="等級",value=network_level)
            embed1.add_field(name="人品",value=k)
            embed1.add_field(name="首次加入 • 最後登入",value=fl+" • "+t)
            await message.edit(embed= embed1)

  @commands.command()
  async def bw(self, ctx, name=None):
    await ctx.send("`🚧指令維修中`")
  #   if name == None:
  #     await message.edit(embed=discord.Embed(description=f":x: | 請輸入一個玩家",color=discord.Color.red()))
  #     return

  #   message = await ctx.send(embed=discord.Embed(description="<a:loading:830383608463228948> | 查詢中 請稍後",color=discord.Color.green()))
  #   try:
  #     data = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{name}").json()
  #   except:
  #     await message.edit(embed=discord.Embed(description=f":x: | 找不到 **{name}** 這個玩家",color=discord.Color.red()))
  #     return
  #   mc = requests.get(f"https://api.hypixel.net/player?key=092f48b3-ea7c-43b8-87b9-b225836ee963&uuid={data['id']}").json()
  #   p = mc["player"]
  #   if p == "null":
  #     await message.edit(embed=discord.Embed(description=f":x: | 找不到 **{name}** 這個玩家",color=discord.Color.red()))
  #     return
  #   else:
  #     if "prefix" in p:
  #       r = "[OWNER]"
  #     else:
  #       if "rank" in p:
  #         if str(p["rank"]) in ranks:
  #            r = ranks[p["rank"]]
  #         else:
  #           r = p["rank"]
  #           else:
  #             if "mostRecentMonthlyPackageRank" in p:
  #               if str(p["mostRecentMonthlyPackageRank"]) in ranks:
  #               r = ranks[p["mostRecentMonthlyPackageRank"]]
  #               else:
  #               r = p["mostRecentMonthlyPackageRank"]
  #                 else:
  #                  if "newPackageRank" in p:
  #                     if str(p["newPackageRank"]) in ranks:
  #                       r = ranks[p["newPackageRank"]]
  #                   else:
  #                     r = ""
  #     s = p['stats']
  #     ac = p['achievements']
  #     lv = ac['bedwars_level']
  #     bwwins = ac['bedwars_wins']
  #     b = s['Bedwars']
  #     bwboxes = b['bedwars_boxes']
  #     winsk = b['winstreak']
  #     con = b['coins']
  #     kills = b['kills_bedwars']
  #     final = b['final_kills_bedwars']
  #     bok = b['beds_broken_bedwars']
  #     embed = discord.Embed(title=f'<:bed:830778190905344030>床戰資料', color=random.randint(0, 0xffffff))
  #     embed.set_thumbnail(url=f"https://crafatar.com/renders/body/{data['id']}")
  #     embed.add_field(name='[Rank]ID', value=f'{r}{name}')
  #     embed.add_field(name='等級', value=lv)
  #     embed.add_field(name='總勝利數', value=bwwins)
  #     embed.add_field(name='獎勵箱數', value=bwboxes)
  #     embed.add_field(name='連勝數', value=winsk)
  #     embed.add_field(name='金幣', value=con)
  #     embed.add_field(name='總擊殺數', value=kills)
  #     embed.add_field(name='最終擊殺數', value=final)
  #     embed.add_field(name='破壞床數', value=bok)
  #     await message.edit (embed = embed)
  @commands.command()
  async def hypimg(self, ctx, name=None):
    if name == None:
      await ctx.send(embed=discord.Embed(description=f":x: | 請輸入一個玩家",color=discord.Color.red()))
    else:
      try:
        url = f'https://api.mojang.com/users/profiles/minecraft/{name}' 
        response = requests.get(url)
        uuid = response.json()['id']
        purl = f'https://hypixel.paniek.de/signature/{uuid}/general-tooltip'
        # embed = discord.Embed(color=random.randint(0, 0xffffff))
        # embed.set_image(url=purl)
        # await ctx.send(embed=embed)
        await ctx.send(purl)
      except:
        await ctx.send(embed=discord.Embed(description=f":x: | 找不到 **{name}** 這個玩家",color=discord.Color.red()))
  
  @commands.command()
  async def hyplv(self, ctx, name):
    try:
      url = f'https://gen.plancke.io/exp/{name}.png'
      embed = discord.Embed(color=random.randint(0, 0xffffff))
      embed.set_image(url=url)
      await ctx.send(embed=embed)
    except:
      await ctx.send(embed=discord.Embed(description=f":x: | 找不到 **{name}** 這個玩家",color=discord.Color.red()))
    
    
    


    



def setup(bot):
  bot.add_cog(Hyp(bot))