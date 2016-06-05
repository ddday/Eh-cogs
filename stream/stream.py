import discord
from discord.ext import commands
from cogs.utils import checks
from __main__ import set_cog, send_cmd_help, settings
from .utils.dataIO import fileIO
import importlib
import traceback
import logging
import asyncio
import threading
import datetime
import glob
import os
import time

log = logging.getLogger("red.owner")

class Stream:
    """A stream set"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @checks.is_owner()
    async def stream(self, ctx, stream=None, *, status=None):
        """Sets red's streaming status

        Leaving this empty will clear it."""

        if status:
            status = status.strip()
            if "twitch.tv/" not in stream:
                stream = "https://www.twitch.tv/" + stream
            await self.bot.change_status(discord.Game(type=1, url=stream, name=status))
            log.debug('Owner has set streaming status and url to "{}" and {}'.format(status, stream))
        else:
            await self.bot.change_status(None)
            log.debug('status cleared by owner')
        await self.bot.say("Done.")

def setup(bot):
    n = Stream(bot)
    bot.add_cog(n)
