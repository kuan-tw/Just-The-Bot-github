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

ranks = {"VIP":"[VIP]","VIP_PLUS":"[VIP+]","MVP":"[MVP]","MVP_PLUS":"[MVP+]","SUPERSTAR":"[MVP++]","YOUTUBER":"[YOUTUBE]","ADMIN":"[ADMIN]"}

class Hyp(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(description="查看玩家狀態或是Hypixel資料",usage="c!mc [玩家名]")
  async def hyp(self, ctx, name):
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
                r = "[OWNER]"
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
            if str(r) == "NORMAL":
                r = ""
            embed1 = discord.Embed(title="Minecraft Hypixel 玩家資料",colour=random.randint(0, 0xffffff))
            embed1.set_thumbnail(url=f"https://crafatar.com/renders/body/{data['id']}")
            embed1.add_field(name="[Rank]Name",value=f"{r}{p['displayname']}")
            embed1.add_field(name="UUID",value=data["id"])
            embed1.add_field(name="等級",value=network_level)
            embed1.add_field(name="人品",value=k)
            embed1.add_field(name="首次加入 • 最後登入",value=fl+" • "+t)
            await message.edit(embed= embed1)

  @commands.command()
  async def bw(self, ctx, name):
    message = await ctx.send(embed=discord.Embed(
            description="<a:loading:830383608463228948> | 查詢中 請稍後",color=discord.Color.green()))
    try:
            data = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{name}").json()
    except:
            await message.edit(embed=discord.Embed(description=f":x: | 找不到 **{name}** 這個玩家",color=discord.Color.red()))
            return
    mc = requests.get(f"https://api.hypixel.net/player?key=092f48b3-ea7c-43b8-87b9-b225836ee963&uuid={data['id']}").json()
    p = mc["player"]
    if "prefix" in p:
                r = "[OWNER]"
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
    s = p['stats']
    ac = p['achievements']
    lv = ac['bedwars_level']
    bwwins = ac['bedwars_wins']
    b = s['Bedwars']
    bwboxes = b['bedwars_boxes']
    winsk = b['winstreak']
    con = b['coins']
    kills = b['kills_bedwars']
    final = b['final_kills_bedwars']
    bok = b['beds_broken_bedwars']

    embed = discord.Embed(title=f'<:bed:830778190905344030>床戰資料', color=random.randint(0, 0xffffff))
    embed.set_thumbnail(url=f"https://crafatar.com/renders/body/{data['id']}")
    embed.add_field(name='[Rank]ID', value=f'{r}{name}')
    embed.add_field(name='等級', value=lv)
    embed.add_field(name='總勝利數', value=bwwins)
    embed.add_field(name='獎勵箱數', value=bwboxes)
    embed.add_field(name='連勝數', value=winsk)
    embed.add_field(name='金幣', value=con)
    embed.add_field(name='總擊殺數', value=kills)
    embed.add_field(name='最終擊殺數', value=final)
    embed.add_field(name='破壞床數', value=bok)
    await message.edit (embed=embed)



    



    


def setup(bot):
  bot.add_cog(Hyp(bot))