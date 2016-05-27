import discord
from discord.ext import commands
from __main__ import send_cmd_help
import aiohttp

class Chucknorris:
    """chucknorris commands."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def chuck(self):
        search = "https://api.chucknorris.io/jokes/random"
        try:
            async with aiohttp.get(search) as r:
                result = await r.json()
            await self.bot.say(result['value'])
        except:
            await self.bot.say("Error.")

def setup(bot):
    n = Chucknorris(bot)
    bot.add_cog(n)