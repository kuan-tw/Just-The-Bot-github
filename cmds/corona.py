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
      await ctx.send(embed=discord.Embed(description=f":x: | 請輸入一個國家",color=discord.Color.red()))
      return
    country = msg
    url = f'https://coronavirus-19-api.herokuapp.com/countries/{country}?'
    response = requests.get(url)
    try:
      ccountry = response.json()['country']
    except:
      await ctx.send(embed=discord.Embed(description=f":x: | 找不到 **{msg}** 這個國家",color=discord.Color.red()))
      return   
    cases = response.json()['cases']
    tcases = response.json()['todayCases']
    deaths = response.json()['deaths']
    tdeaths = response.json()['todayDeaths']
    recovered = response.json()['recovered']
    
    embed = discord.Embed(title='武漢肺炎疫情', description=f'國家:{ccountry}', colour=random.randint(0, 0xffffff))
    embed.set_thumbnail(url="https://www.nord24.de/Bilder/Die-Zahl-der-im-Zusammenhang-mit-dem-Corona-Virus-69556.jpg")
    embed.add_field(name='總確診數', value=f'`{cases}`', inline=True)
    embed.add_field(name='今日確診', value=f'`{tcases}`', inline=True)
    embed.add_field(name='死亡數', value=f'`{deaths}`', inline=True)
    embed.add_field(name='今日死亡', value=f'`{tdeaths}`', inline=True)
    embed.add_field(name='解除隔離', value=f'`{recovered}`', inline=True)
    await ctx.send(embed=embed)

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
