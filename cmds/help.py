import discord
from discord.ext import commands
import json
import asyncio
import datetime
import time
import random
import os


class Help(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def help(self, ctx):
		embed = discord.Embed(
		    title='指令列表', description='prefix:=', color=random.randint(1, 300))
		embed.add_field(name='主要指令', value='`ping` `inv` `say` `thinking` ', inline=True)
		embed.add_field(name='資訊類', value='`user` `server`', inline=True)
		embed.add_field(name='管理員指令', value='`anno`', inline=True)
		embed.set_footer(text='made by kuan 🇹🇼#6503')
    await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Help(bot))
