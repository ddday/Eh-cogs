import discord
from discord.ext import commands

class Id:
    """id Cog"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def id(self, ctx):
        """Tells the invoker how to get IDs"""
        await self.bot.reply("To get someone's ID  put a backslash and an atmention together, like this: `\@anomaly'")

def setup(bot):
    n = Id(bot)
    bot.add_cog(n)
