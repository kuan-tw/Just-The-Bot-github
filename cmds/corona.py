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
from googleapiclient.discovery import build

key = 'AIzaSyB6JYaKcPcJmJcdmNGLJUCtqPslB0lyr3k'

class Corona(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def corona(self, ctx, *, msg):
    country = msg
    url = f'https://coronavirus-19-api.herokuapp.com/countries/{country}?'
    response = requests.get(url)
    cases = response.json()['cases']
    tcases = response.json()['todayCases']
    deaths = response.json()['deaths']
    tdeaths = response.json()['todayDeaths']
    recovered = response.json()['recovered']
    embed = discord.Embed(title='武漢肺炎疫情', description=f'國家:{country}', colour=random.randint(0, 0xffffff))
    embed.set_thumbnail(url="https://www.nord24.de/Bilder/Die-Zahl-der-im-Zusammenhang-mit-dem-Corona-Virus-69556.jpg")
    embed.add_field(name='總確診數', value=cases, inline=True)
    embed.add_field(name='今日確診', value=tcases, inline=True)
    embed.add_field(name='死亡數', value=deaths, inline=True)
    embed.add_field(name='今日死亡', value=tdeaths, inline=True)
    embed.add_field(name='解除隔離', value=recovered, inline=True)
    await ctx.send(embed=embed)

  @commands.command()
  async def weather(self, ctx, *,msg: str):
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
            weather_description = z[0]["description"]
            weather_description = z[0]["description"]
            embed = discord.Embed(title=f"{city_name}的天氣",
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
        await channel.send("City not found.")
    


def setup(bot):
  bot.add_cog(Corona(bot))
