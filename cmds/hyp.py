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

ranks = {"VIP":"<:VIP1:849149582675148823><:VIP2:849149665844920330><:VIP3:849149715769065472>","VIP_PLUS":"<:VIP1p:849162779118403615><:VIP2p:849162636959678504><:VIP3p:849162164627177553>","MVP":"<:MVP1:849163934434590720><:MVP2:849164000885342239><:MVP3:849164044732858368>","MVP_PLUS":f"[MVP+]","SUPERSTAR":"[MVP++]","YOUTUBER":"<:yt1:849165730931146773><:yt2:849165834160832520><:yt3:849165878787833857><:yt4:849165926141526017><:yt5:849165958278938645>","ADMIN":"<:admin1:849179000940265492><:admin2:849179041550041119><:admin3:849179078467911680><:admin4:849179126095282180>"}
rankpluscolor = {"BLACK": "<:mvp_plus1:849952191951011870><:mvp_plus2:849952252269035521><:mvp_plus3:849952501280014396><:plus_black:849952545278525451>"}
rs = ["VIP", "VIP_PLUS"]





class Hyp(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(description="查看玩家狀態或是Hypixel資料",usage="=hyp [玩家名]")
  async def hyp(self, ctx, name=None):
    # await ctx.send('`🚧指令維修中🚧`')
    if name == None:
      await ctx.send(embed=discord.Embed(description=f":x: | 請輸入一個玩家",color=discord.Color.red()))
    else:
          message = await ctx.send(embed=discord.Embed(
              description="<a:loading:830383608463228948> | 查詢中 請稍後",color=discord.Color.green()))
          try:
              data = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{name}").json()
          except:
              await message.edit(embed=discord.Embed(description=f":x: | 找不到 **{name}** 這個玩家",color=discord.Color.red()))
              return
          mc = requests.get(f"https://api.hypixel.net/player?key=092f48b3-ea7c-43b8-87b9-b225836ee963&uuid={data['id']}").json()
          try:
            guild = requests.get(f"https://api.hypixel.net/guild?key=092f48b3-ea7c-43b8-87b9-b225836ee963&player={data['id']}").json()
            g = guild['guild']
            gn = g['name']
          except:
            gn = "無公會"
          try:
            tag = f"[{g['tag']}]"
          except:
            tag = ""
          p = mc["player"]
          status = requests.get(f"https://api.hypixel.net/status?key=092f48b3-ea7c-43b8-87b9-b225836ee963&uuid={data['id']}").json()
          sess = status['session']
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
                  r = ranks[p["rank"]]
                else:
                    if "mostRecentMonthlyPackageRank" in p:
                      if p['monthlyPackageRank'] != "NONE":
                        r = ranks[p["mostRecentMonthlyPackageRank"]]
                      else:
                          r = ranks[p['newPackageRank']]
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
              if sess['online'] == True:
                stat = "<a:online:827478619819212812>"
                t = "在線"
              else:
                stat = "<a:offline:827478874627112990>"
              embed1 = discord.Embed(title=f"{stat}{r}{p['displayname']} {tag}",colour=random.randint(0, 0xffffff))
              embed1.set_thumbnail(url=f"https://crafatar.com/renders/body/{data['id']}")
              embed1.add_field(name="UUID",value=data["id"])
              embed1.add_field(name="等級",value=network_level)
              embed1.add_field(name="人品",value=k)
              embed1.add_field(name="公會",value=gn)
              embed1.add_field(name="首次加入 • 最後登入",value=fl+" • "+t)
              await message.edit(embed= embed1)
  @commands.command()
  async def bw(self, ctx, name=None):
    # await ctx.send('`🚧指令維修中🚧`')
    t = 0
    if name == None:
      await ctx.send(embed=discord.Embed(description=f":x: | 請輸入一個玩家",color=discord.Color.red()))
    else:
      message = await ctx.send(embed=discord.Embed(description="<a:loading:830383608463228948> | 查詢中 請稍後",color=discord.Color.green()))
      try:
        data = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{name}").json()
      except:
        await message.edit(embed=discord.Embed(description=f":x: | 找不到 **{name}** 這個玩家",color=discord.Color.red()))
        return
      mc = requests.get(f"https://api.hypixel.net/player?key=092f48b3-ea7c-43b8-87b9-b225836ee963&name={name}").json()
      p = mc["player"]
      if "rank" not in p:
        r = ""
      if "prefix" in p:
        if p['prefix'] == "§c[OWNER]":
          r = "<:owner1:849196627642155028><:owner2:849196670796562442><:owner3:849196722827558943><:owner4:849196873817784351>"
        elif p['prefix'] == "§d[PIG§b+++§d]" :
          r = "<:pig1:849180613419991070><:pig2:849180648426045500><:pig3:849180680104968192><:pig4:849180713316253696>"
        elif p['prefix'] == "§6[EVENTS]":
          r = "<:ev1:850715152944332842><:ev2:850715222225584159><:ev3:850715281491230740><:ev4:850715317066792970>"
      else:
        if "rank" in p:
          r = ranks[p["rank"]]
        else:
          if "mostRecentMonthlyPackageRank" in p:
            if p['monthlyPackageRank'] != "NONE":
              r = ranks[p["mostRecentMonthlyPackageRank"]]
            else:
              r = ranks[p['newPackageRank']]
          else:
            if "newPackageRank" in p:
              if str(p["newPackageRank"]) in ranks:
                r = ranks[p["newPackageRank"]]
              else:
                r = ""
    if p == "null":
      await message.edit(embed=discord.Embed(description=f":x: | 找不到 **{name}** 這個玩家",color=discord.Color.red()))
    else:
      try:
        adv = p['achievements'] 
        status = p['stats']
        bw = status['Bedwars']
      except:
        await message.edit(embed=discord.Embed(description=f":x: | 找不到 **{name}** 這個玩家",color=discord.Color.red()))
      try:
        name = p['displayname']
      except:
        await message.edit(embed=discord.Embed(description=f":x: | 找不到 **{name}** 這個玩家",color=discord.Color.red()))
      try:
        try:
          lvl = adv['bedwars_level']
        except:
          lvl = "0"
        try:
          wins = adv['bedwars_wins']
        except:
          wins = "0"
        try:
          totalplaycount = bw['games_played_bedwars_1']
        except:
          totalplaycount = "0"
        try:
          winsk = bw['winstreak']
        except:
          winsk = "0"
        try:
          kills = bw['kills_bedwars']
        except:
          kills = "0"
        try:
          final = bw['final_kills_bedwars']
        except:
          final = "0"
        try:
          broken = bw['beds_broken_bedwars'] 
        except:
          broken = "0"
        try:
          dea = bw['deaths_bedwars']
        except:
          dea = "0"
        try:
          fdea = bw['final_deaths_bedwars']
        except:
          fdea = "0"
        #Page 1
        #page 2
        #solo bw
        try:
          swsk = bw['eight_one_winstreak']
        except:
          swsk = "0"
        try:
          sbk = bw['eight_one_beds_broken_bedwars']
        except:
          sbk = "0"
        try:
          sd = bw['eight_one_deaths_bedwars']
        except: 
          sd = "0"
        try:
          sfd = bw['eight_one_final_deaths_bedwars']
        except:
          sfd = "0"
        try:
          sk = bw['eight_one_kills_bedwars']
        except:
          sk = "0"
        try:
          sfk = bw['eight_one_final_kills_bedwars']
        except:
          sfk = "0"
        try:
          sp = bw['eight_one_games_played_bedwars']
        except:
          sp = "0"
        try:
          sl = bw['eight_one_losses_bedwars']
        except:
          sl = "0"
        #doable bw
        try:
          dp = bw['eight_two_games_played_bedwars']
        except:
          d = "0"
        try:
          dk = bw['eight_two_kills_bedwars']
        except:
          dk = "0"
        try:
          dwsk = bw['eight_two_winstreak']
        except:
          dwsk = "0"
        try:
          dw = bw['eight_two_wins_bedwars']
        except:
          dw = "0"
        try:
          dfk = bw['eight_two_final_kills_bedwars']
        except:
          dfk = "0"
        try:
          dd = bw['eight_two_deaths_bedwars']
        except:
          dd = "0"
        try:
          dfd = bw['eight_two_final_deaths_bedwars']
        except:
          dfd = "0"
        try:
          db = bw['eight_two_beds_broken_bedwars']
        except:
          db = "0"
      except:
        await message.edit(embed=discord.Embed(description=f":x: | 找不到 **{name}** 這個玩家",color=discord.Color.red()))
      try:
        sw = sp - sl
        sokdr = round(int(sk) / int(sd), 2)
        sofkdr = round(int(sfk) / int(sfd), 2)
        sotok = sk + sfk
        dkdr = round(int(dk) / int(dd), 2)
        dfkdr = round(int(dfk) / int(dfd), 2)
        dtk = dk + dfk
        totalkills = int(kills) + int(final)
        kdr = round(int(kills) / int(dea), 2)
        fkdr = round(int(final) / int(fdea), 2)
      except:
        try:
          sw = sp - sl
        except:
          sw = "N/A"
        try:
          sokdr = round(int(sk) / int(sd))
        except:
          sokdr = "N/A"
        try:
          sofkdr = round(int(sfk) / int(sfd), 2)
        except:
          sofkdr = "0"
        try:
          sotok = int(sk) + int(sfk)
        except:
          sotok = "0"
        try:
          dkdr = round(int(dk) / int(dd), 2)
        except:
          dkdr = "0"
        try:
          dfkdr = round(int(dfk) / int(dfd), 2)
        except:
          dfkdr = "0"
        try:
          dtk = int(dk) + int(dfk)
        except:
          dtk = "0"
        try:
          totalkills = int(kills) + int(final)
        except:
          totalkills = "0"
        try:
          kdr = round(int(kills) / int(dea), 2)
        except:
          kdr = "0"
        try:
          fkdr = round(int(final) / int(fdea), 2)
        except:
          fkdr = "0"
    o = discord.Embed(title=f'<:bed:830778190905344030>[{lvl}☆] {r}{name}', color=random.randint(0, 0xffffff))
    o.set_thumbnail(url=f"https://crafatar.com/renders/body/{data['id']}")
    o.add_field(name='遊玩次數', value=totalplaycount)
    o.add_field(name='勝利數', value=wins) 
    o.add_field(name='總擊殺數', value=f'{totalkills}\n。擊殺數-{kills}\n。KDR-{kdr}\n。最終擊殺數-{final}\n。FKDR-{fkdr}')
    o.add_field(name='破壞床數', value=broken) 
    o.set_footer(text='頁數 1/2')
    await message.edit(embed=o) 
    await message.add_reaction('1️⃣')
    await message.add_reaction('2️⃣')
    reactmoji = ["1️⃣","2️⃣"]
    t = discord.Embed(title=f'[{lvl}☆]{r}{name}', color=random.randint(0, 0xffffff))
    t.set_thumbnail(url=f"https://crafatar.com/renders/body/{data['id']}")
    t.add_field(name=' 單人模式 ', value=f'遊玩次數-{sp}\n勝利數-{sw}\n總擊殺數-{sotok}\n。擊殺數-{sk}\n。最終擊殺數-{sfk}\n。KDR-{sokdr}\n。FKDR-{sofkdr}\n破壞床數-{sbk}')
    t.add_field(name=' 雙人模式 ', value=f'遊玩次數-{dp}\n勝利數-{dw}\n總擊殺數-{dtk}\n。擊殺數-{dk}\n。最終擊殺數-{dfk}\n。KDR-{dkdr}\n。FKDR-{dfkdr}\n破壞床數-{db}')
    t.set_footer(text=f'頁數 2/2 ')

    def check_react(reaction, user):
      if reaction.message.id != message.id:
        return False
      if user != ctx.message.author:
        return False
      if str(reaction.emoji) not in reactmoji:
        return False
      return True
    while True:
      try:
        res, user = await self.bot.wait_for('reaction_add', check=check_react)
      except asyncio.TimeoutError:
        return await message.clear_reactions()
      if user != ctx.message.author:
        pass
      elif '2️⃣' in str(res.emoji):
        await message.remove_reaction("2️⃣",user)
        await message.edit(embed=t)
        page = 2
      if '1️⃣' in str(res.emoji) and page == 2:
        await message.remove_reaction("1️⃣",user)
        await message.edit(embed=o)
        page = 1

  
  

    


    
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

  @commands.command()
  async def skyblock(self, ctx):
    url = 'https://api.hypixel.net/skyblock/news?key=092f48b3-ea7c-43b8-87b9-b225836ee963'
    response = requests.get(url)
    i = response.json()['items']
    p = i[0]
    link = p['link']
    text = p['text']
    title = p['title']
    embed = discord.Embed(title=title,color=random.randint(0, 0xffffff))
    embed.add_field(name='時間', value=text)
    embed.add_field(name='連結', value=link)
    await ctx.send(embed=embed)
    



  
    
    
    


    



def setup(bot):
  bot.add_cog(Hyp(bot))