from typing import Any
from discord import Client, Intents


class DiscordNewsBotClient(Client):
    def __init__(self, *, intents: Intents, **options: Any) -> None:
        super().__init__(intents=intents, **options)

    async def on_ready(self) -> None:
        print(f'We have logged in as {self.user}')
