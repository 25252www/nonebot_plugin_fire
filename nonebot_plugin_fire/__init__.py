import asyncio
import random

import nonebot
from nonebot import require, get_bot
from nonebot.log import logger

scheduler = require("nonebot_plugin_apscheduler").scheduler
fire_user_id = nonebot.get_driver().config.fire_user_id


@scheduler.scheduled_job("cron", day="*")
async def run_every_second():
    bot = get_bot()
    await asyncio.sleep(random.randint(1, 10))
    logger.info("发送火花")
    await bot.call_api("send_msg", user_id=fire_user_id, message="/echo 花花")
