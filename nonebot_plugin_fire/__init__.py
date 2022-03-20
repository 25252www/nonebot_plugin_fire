import asyncio
import random
from nonebot import require, get_bot, get_driver
from nonebot.log import logger


try:
    scheduler = require("nonebot_plugin_apscheduler").scheduler
except BaseException:
    scheduler = None

logger.opt(colors=True).info(
    "已检测到软依赖<y>nonebot_plugin_apscheduler</y>, <g>开启定时任务功能</g>"
    if scheduler
    else "未检测到软依赖<y>nonebot_plugin_apscheduler</y>，<r>禁用定时任务功能</r>"
)

fire_user_id = get_driver().config.fire_user_id


async def fire_scheduler():
    sendSuccess = False
    while not sendSuccess:
        try:
            await asyncio.sleep(random.randint(1, 10))
            await get_bot().send_private_msg(user_id=fire_user_id, message="/echo 花花")  # 当未连接到onebot.v11协议端时会抛出异常
            logger.info("发送火花")
            sendSuccess = True
        except ValueError as e:
            logger.error("ValueError:{}", e)
            logger.error("续火花插件获取bot失败，1s后重试")
            await asyncio.sleep(1)  # 重试前时延，防止阻塞


if scheduler:
    scheduler.add_job(fire_scheduler, "cron", hour="0", id="fire_scheduler")
