from aiogram import Bot

from tgbot.services import broadcaster


async def on_startup_notify(bot: Bot, admin_ids: list[int]):
    await broadcaster.broadcast(bot, admin_ids, "The bot has been started!")
