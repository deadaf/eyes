from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core import Eyes

from disnake.ext import commands
import disnake


class EyeEvents(commands.Cog):
    def __init__(self, bot: Eyes):
        self.bot = bot

    @commands.Cog.listener()
    async def on_presence_update(self, before: disnake.Member, after: disnake.Member):
        ...


def setup(bot: Eyes):
    bot.add_cog(EyeEvents(bot))
