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
    else:
      url = f'https://corona.lmao.ninja/v3/covid-19/countries/{msg}' 
      response = requests.get(url)
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

    


def setup(bot):
  bot.add_cog(Corona(bot))
