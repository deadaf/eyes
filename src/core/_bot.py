from disnake.ext import commands
import typing
import cogs
import asyncio

import disnake

from tinydb import TinyDB

__all__ = ("Eyes", "bot")
on_startup: typing.List[typing.Callable[["Eyes"], typing.Coroutine]] = []


class Eyes(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(
            command_prefix=commands.when_mentioned_or("e"),
            case_insensitive=True,
            strip_after_prefix=True,
            test_guilds=[746337818388987967],
            reload=True,
            intents=disnake.Intents.all(),
            **kwargs,
        )

        self.loop = asyncio.get_event_loop()
        self.db = TinyDB("./src/db/data.json")

        for coro_func in on_startup:
            self.loop.create_task(coro_func(self))

    @on_startup.append
    async def __load_extensions(self):
        for _ in cogs.__loadable__:
            self.load_extension(_)
            print(f"Loaded extension: {_}")

    async def on_ready(self):
        print("Logged in as {0} ({0.id})".format(self.user))


bot = Eyes()
