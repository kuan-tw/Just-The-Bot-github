import discord
from discord.ext import commands
import datetime
import re
import random

# road ad regex, thanks road
invitere = r"(?:https?:\/\/)?discord(?:\.gg|app\.com\/invite)?\/(?:#\/)([a-zA-Z0-9-]*)"
# my own regex
invitere2 = r"(http[s]?:\/\/)*discord((app\.com\/invite)|(\.gg))\/(invite\/)?(#\/)?([A-Za-z0-9\-]+)(\/)?"


class Snipe(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.snipes = {}

        @bot.listen('on_message_delete')
        async def on_message_delete(msg):
            if msg.author.bot:
                return
            self.snipes[msg.channel.id] = msg



    def sanitise(self, string):
        if len(string) > 1024:
            string = string[0:1021] + "..."
        string = re.sub(invitere2, '(此為邀請訊息)', string)
        return string

    @commands.command()
    async def snipe(self, ctx):
        '"Snipes" someone\'s message that\'s been edited or deleted.'
        try:
            snipe = self.snipes[ctx.channel.id]
        except KeyError:
            return await ctx.send('❌找不到被刪除的訊息')
        if snipe is None:
            return await ctx.send('❌找不到被刪除的訊息')
        # there's gonna be a snipe after this point
        emb = discord.Embed()
        if type(snipe) == list:  # edit snipe
            emb.set_author(
                name=str(snipe[0].author),
                icon_url=snipe[0].author.avatar_url)
            emb.colour=random.randint(0, 0xffffff)
            emb.add_field(
                name='Before',
                value=self.sanitise(snipe[0].content),
                inline=False)
            emb.add_field(
                name='After',
                value=self.sanitise(snipe[1].content),
                inline=False)
            emb.timestamp = snipe[0].created_at
        else:  # delete snipe
            emb.set_author(
                name=str(snipe.author),
                icon_url=snipe.author.avatar_url)
            if snipe.attachments:
              emb.description = self.sanitise(snipe.content)
              at = []
              for im in snipe.attachments:
                at.append(f'[{im.filename}](https://media.discordapp.net{im.url[26:]})')
                i = f"https://media.discordapp.net{im.url[26:]}"
                emb.set_image(url=i)
              emb.add_field(name="📎附件", value= "\n".join(at))
            else:
              emb.description = self.sanitise(snipe.content)
            emb.colour = snipe.author.colour
            emb.timestamp = snipe.created_at
        await ctx.send(embed=emb)
        self.snipes[ctx.channel.id] = None


def setup(bot):
  bot.add_cog(Snipe(bot))