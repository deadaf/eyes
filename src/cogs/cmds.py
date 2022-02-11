from __future__ import annotations

from typing import TYPE_CHECKING
import disnake

if TYPE_CHECKING:
    from core import Eyes

from disnake.ext import commands


class EyeCommands(commands.Cog):
    def __init__(self, bot: Eyes):
        self.bot = bot

    @commands.slash_command()
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        """Get the bot's current websocket latency."""
        await inter.response.send_message(
            f"Pong! {round(self.bot.latency * 1000)}ms", ephemeral=True
        )


def setup(bot: Eyes):
    bot.add_cog(EyeCommands(bot))
