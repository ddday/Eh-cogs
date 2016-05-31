import discord
from discord.ext import commands
from .utils import checks


class Invite:
    """Runs a command in the terminal"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @checks.admin_or_permissions(manage_server=True)
    async def makeinvite(self, ctx, *, server):
        try:
            serverobject = discord.utils.get(self.bot.servers, name=server)
            invite = await self.bot.create_invite(serverobject, max_age=0)
            await self.bot.send_message(ctx.message.author, invite)
        except:
            await self.bot.say("No server found or invalid permissions")

def setup(bot):
    n = Invite(bot)
    bot.add_cog(n)
    