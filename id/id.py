import discord
from discord.ext import commands

class id:
    """id Cog"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def id(self, ctx):
        """id the user"""
        id = ctx.message.author.id
        await self.bot.say("Your ID is: " + id)

def setup(bot):
    n = id(bot)
    bot.add_cog(n)