import discord
from discord.ext import commands
from discord.ext import tasks, commands
import json
import asyncio
import datetime
import time
import os
import math
import random
import io
import requests

ntc = {"indea","n.korea"}

key = 'AIzaSyB6JYaKcPcJmJcdmNGLJUCtqPslB0lyr3k'


class Corona(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def corona(self, ctx, *, msg=None):
    if msg == None:
      res = requests.get('https://corona.lmao.ninja/v3/covid-19/all')
      cases = res.json()['cases']
      today = res.json()['todayCases']
      deaths = res.json()['deaths']
      tdeaths = res.json()['todayDeaths']
      rev = res.json()['recovered']
      trev = res.json()['todayRecovered']
      tests = res.json()['tests']
      embed = discord.Embed(title=f'世界疫情', color=random.randint(0, 0xffffff))
      embed.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQekmk0lSxs2C5lpjTqca-G6FgT0Gl8Xg3t_Q&usqp=CAU')
      embed.add_field(name='累計確診  ', value=cases)
      embed.add_field(name='今日確診  ', value=today)
      embed.add_field(name='累計死亡  ', value=deaths)
      embed.add_field(name='今日死亡  ', value=tdeaths)
      embed.add_field(name='治癒  ', value=f'{rev}')
      embed.add_field(name='今日治癒  ', value=trev)
      embed.add_field(name='篩檢數  ', value=tests)
      await ctx.send(embed=embed)
    elif msg.lower() in ntc:
      await ctx.send(embed=discord.Embed(description=f":cry: | 這個資料庫並沒有提供這個國家的疫情喔 sorry~",color=discord.Color.red()))
    else:
      url = f'https://corona.lmao.ninja/v3/covid-19/countries/{msg}'
      url2 = f'https://disease.sh/v3/covid-19/vaccine/coverage/countries/{msg}?lastdays=1&fullData=false'
      response = requests.get(url)
      v = requests.get(url2)
      try:
        country = response.json()['country']
        ci = response.json()['countryInfo']
        flag = ci['flag']
        cases = response.json()['cases']
        today = response.json()['todayCases']
        deaths = response.json()['deaths']
        tdeaths = response.json()['todayDeaths']
        rev = response.json()['recovered']
        trev = response.json()['todayRecovered']
        tests = response.json()['tests']
        embed = discord.Embed(title=f'{country}的疫情', color=random.randint(0, 0xffffff))
        embed.set_thumbnail(url=flag)
        embed.add_field(name='累計確診', value=cases)
        embed.add_field(name='今日確診', value=today)
        embed.add_field(name='累計死亡', value=deaths)
        embed.add_field(name='今日死亡', value=tdeaths)
        embed.add_field(name='治癒', value=f'{rev}')
        embed.add_field(name='今日治癒', value=trev)
        embed.add_field(name='篩檢數', value=tests)
        await ctx.send(embed=embed)
      except:
        await ctx.send(embed=discord.Embed(description=f":x: | 未知的國家",color=discord.Color.red()))
    
      


  @commands.command()
  async def weather(self, ctx, *,msg: str = None):
    if msg == None:
      await ctx.send(embed=discord.Embed(description=f":x: | 請輸入一個城市",color=discord.Color.red()))
      return
    api_key = "00f58b31fe4a45b121e3e003ab28cc6f"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    response = requests.get(base_url)
    lang = 'zh_tw'
    city_name = msg
    complete_url = base_url + "&q=" + city_name + '&lang=' + lang + "&appid=" + api_key
    response = requests.get(complete_url)
    x = response.json()
    channel = ctx.message.channel
    if x["cod"] != "404":
        async with channel.typing():
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature_celsiuis = str(round(current_temperature - 273.15))
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            s = x["sys"]
            c = s["country"]
            weather_description = z[0]["description"]
            weather_description = z[0]["description"]
            embed = discord.Embed(title=f"{city_name},{c}",
                              color=ctx.guild.me.top_role.color,
                              timestamp=ctx.message.created_at,)
            embed.add_field(name="天氣", value=f"**{weather_description}**", inline=False)
            embed.add_field(name="溫度(C)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
            embed.add_field(name="濕度(%)", value=f"**{current_humidity}%**", inline=False)
            embed.add_field(name="氣壓(hPa)", value=f"**{current_pressure}hPa**", inline=False)
            embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            await channel.send(embed=embed)
    else:
        await ctx.send(embed=discord.Embed(description=f":x: | 找不到 **{msg}** 這個城市",color=discord.Color.red()))

  @commands.command()
  async def eq(self, ctx):
    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0015-001?Authorization=CWB-B13B35B2-04DC-4338-80F2-CCCE784C5BEE"
    response = requests.get(url)
    r = response.json()
    rec = r['records']
    eq = rec['earthquake']
    z = eq[0]
    eqno = z['earthquakeNo']
    eqrc = z['reportContent']
    img = z['reportImageURI']
    q = z['earthquakeInfo']
    ti = q['originTime']
    d = q['depth']
    ep = q['epiCenter']
    mag = q['magnitude']
    
    dp = d['value']
    loc = ep['location']
    val = mag['magnitudeValue']

    

    embed = discord.Embed(title='最近的有感地震報告', color=random.randint(0, 0xffffff))
    embed.add_field(name='編號', value=eqno)
    embed.add_field(name='地震', value=eqrc)
    embed.add_field(name='位置', value=loc)
    embed.add_field(name='時間', value=ti)
    embed.add_field(name='深度', value=f'{dp} 公里')
    embed.add_field(name='芮氏規模', value=val)
    embed.set_image(url=f"{img}")
    embed.set_footer(text='中央氣象局')
    await ctx.send(embed=embed)

  @commands.command()
  async def alert(self, ctx):
    try:
      while True:
        channel = self.bot.get_channel(875237868786823219)
        url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/W-C0033-002?Authorization=CWB-B13B35B2-04DC-4338-80F2-CCCE784C5BEE"
        response = requests.get(url)
        r = response.json()
        rec = r['records']
        re = rec['record']
        a = re[0]
            
        data = a['datasetInfo']
        des = data['datasetDescription']
        vt = data['validTime']
            
        st = vt['startTime']
        et = vt['endTime']
            
        c = a['contents']
        con = c['content']
            
        text = con['contentText']
        embed = discord.Embed(title=des,description=text,color=random.randint(0, 0xffffff))
        embed.add_field(name='時間', value=f'{st} ~ {et}')
        await channel.send(embed=embed)
        await asyncio.sleep(600)
    except:
      while True:
        await channel.send(embed=discord.Embed(title='目前無天氣特報',color=random.randint(0, 0xffffff)))
        await asyncio.sleep(600)

  @commands.command()
  async def twrain(self, ctx, sid= None, mon=None):
    if sid == None:
      await ctx.send(embed=discord.Embed(description=f":x: | 請輸入測站ID",color=discord.Color.red()))
    if mon == None:
      await ctx.send(embed=discord.Embed(description=f":x: | 請輸入月份",color=discord.Color.red()))
    try:
      url = f'https://opendata.cwb.gov.tw/api/v1/rest/datastore/C-B0025-001?Authorization=CWB-B13B35B2-04DC-4338-80F2-CCCE784C5BEE&format=JSON&stationId={sid}&statistics=true'
      response = requests.get(url)
      r = response.json()
      rec = r['records']
      loc = rec['location']
      a = loc[0]
      s = a['station']

      stid = s['stationID']
      stname = s['stationName']
      stype = s['stationAttribute']

      o = a['stationObsStatistics']
      p = o['precipitation']
      m = p['monthly']

      if mon == "1":
        nl = m[0]
      elif mon == "2":
        nl = m[1]
      elif mon == "3":
        nl = m[2]
      elif mon == "4":
        nl = m[3]
      elif mon == "5":
        nl = m[4]
      elif mon == "6":
        nl = m[5]
      elif mon == "7":
        nl = m[6]
      elif mon == "8":
        nl = m[7]
      elif mon == "9":
        nl = m[8]
      elif mon == "10":
        nl = m[9]
      elif mon == "11":
        nl = m[10]
      elif mon == "12":
        nl = m[11]
      else:
        await ctx.send(embed=discord.Embed(description=f":x: | 找不到資料",color=discord.Color.red()))

      ymon = nl['dataYearMonth']
      total = nl['total']

      embed = discord.Embed(title='全台雨量觀測',color=random.randint(0, 0xffffff))
      embed.add_field(name='測站', value=f'測站ID - {stid}\n名稱 - {stname} \n 類別 - {stype}')
      embed.add_field(name=ymon, value=f'{total} mm')
      embed.set_thumbnail(url="https://i0.wp.com/static.fotor.com.cn/assets/stickers/51b26dd8-6229-4308-8204-88cd7c6b5386_thumb.png")
      await ctx.send(embed=embed)
    except:
      await ctx.send(embed=discord.Embed(description=f":x: | 未知的測站ID([ID列表](https://e-service.cwb.gov.tw/wdps/obs/state.htm)) \n **列表中的測站不一定全部都可查詢**",color=discord.Color.red()))






  
    
 


  




    


def setup(bot):
  bot.add_cog(Corona(bot))
