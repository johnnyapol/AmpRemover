#!/usr/bin/python3
'''
    https://github.com/johnnyapol/discord-amputator
    License: GPL v3.0
'''

import asyncio
import discord
from discord.ext import commands
import logging
import traceback
import util
import os

async def run(bot):
    try:
        await bot.start(os.getenv('DISCORD_BOT_TOKEN'))
    except BaseException as e:
        print(e)
        await bot.logout()
    

class AmputatorBot(commands.Bot):
    def __init__(self):
        super().__init__(
        command_prefix="amp!",
        case_insensitive=True,
        description="Protecting the Open Web!")

    async def on_message(self, message):
        if util.check_if_amp(message.content):
            urls = util.get_amp_urls(message.content)
            non_amp = util.get_canonicals(urls, False)

            msg_text = "Non-AMP Urls:"
            base_len = len(msg_text)

            for url in non_amp:
                if len(url) == 0:
                    continue
                msg_text = f"{msg_text}\n <{url}>"

            if (len(msg_text) != base_len):
                await message.channel.send(msg_text)

asyncio.get_event_loop().run_until_complete(run(AmputatorBot()))
