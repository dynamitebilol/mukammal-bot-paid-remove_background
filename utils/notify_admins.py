import logging

from aiogram import Dispatcher
from loader import bot
from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
        try:
            await bot.send_message(chat_id=ADMINS[0], text ='Bot started')

        except Exception as err:
            logging.exception(err)
