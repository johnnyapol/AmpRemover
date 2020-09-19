#!/usr/bin/python3
"""
    https://github.com/johnnyapol/discord-amputator
    License: GPL v3.0
"""

import asyncio
import discord
from discord.ext import commands
import logging
import traceback
import util
import os

import apple_news
import twitter


async def run(bot):
    try:
        await bot.start(os.getenv("DISCORD_BOT_TOKEN"))
    except BaseException as e:
        print(e)
        await bot.logout()


class AmputatorBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="amp!",
            case_insensitive=True,
            description="Protecting the Open Web!",
        )

    async def on_message(self, message):
        non_amp = []
        split = message.content.splitlines()
        for content in split:
            if util.check_if_amp(content):
                non_amp.extend(util.get_canonicals(util.get_amp_urls(content), False))
            if apple_news.check_if_appl(content):
                non_amp.extend(apple_news.get_urls(content))
            if twitter.check_if_tco(content):
                non_amp.extend(twitter.get_urls(content))

        msg_text = "Non-AMP Urls:"
        base_len = len(msg_text)

        for url in non_amp:
            if len(url) == 0:
                continue
            msg_text = f"{msg_text}\n <{url}>"

        if len(msg_text) != base_len:
            await message.channel.send(msg_text)


asyncio.get_event_loop().run_until_complete(run(AmputatorBot()))
