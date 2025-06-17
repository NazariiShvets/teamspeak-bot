from __future__ import annotations

import asyncio
import os

from tsbot import TSBot, TSCtx, query

TS_CONFIG = {
    "username": os.getenv("TS_SERVER_QUERY_USERNAME"),
    "password": os.getenv("TS_SERVER_QUERY_PASSWORD"),
    "address": os.getenv("TS_ADDRESS"),
    "port": int(os.getenv("TS_PORT")),
    "nickname": os.getenv("TS_NICKNAME"),
    "protocol": os.getenv("TS_PROTOCOL")
}

bot = TSBot(**TS_CONFIG)


@bot.command("hello")
async def hello_world(bot: TSBot, ctx: TSCtx):
    await bot.respond(ctx, f"Hello {ctx['invokername']}!")


@bot.on("cliententerview")
async def poke_on_enter(bot: TSBot, ctx: TSCtx):
    poke_query = query("clientpoke").params(clid=ctx["clid"], msg="Welcome to the server!")
    await bot.send(poke_query)

asyncio.run(bot.run())