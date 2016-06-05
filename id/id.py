import discord
from discord.ext import commands

class Id:
    """id Cog"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def id(self, ctx):
        """Tells the invokers ID"""
        id = ctx.message.author.id
        await self.bot.say("Your ID is: " + id)

def setup(bot):
    n = Id(bot)
    bot.add_cog(n)
