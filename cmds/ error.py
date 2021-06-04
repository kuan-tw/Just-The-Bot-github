import discord

from discord.ext import commands

class Error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
           return
        if isinstance(error, commands.errors.CheckFailure):
            await ctx.send(embed=discord.Embed(description=":x: | 你沒有權限使用此指令", color=discord.Color.red()))
        else:
            embed=discord.Embed(title=':x: | 指令錯誤', color=discord.Color.red())
            embed.add_field(name='錯誤碼', value=error)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Error(bot))