import discord
from discord.ext import commands
from __main__ import send_cmd_help
import aiohttp

class Thisforthat:
    """Fun command."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def this(self):
        search = "http://itsthisforthat.com/api.php?json"
        try:
            async with aiohttp.get(search) as r:
                result = await r.json()
            await self.bot.say('This: ' + result['this'])
            await self.bot.say('That: ' + result['that'])
        except:
            await self.bot.say("Error.")

def setup(bot):
    n = Thisforthat(bot)
    bot.add_cog(n)
