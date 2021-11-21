import sqlite3
from data.config import ADMINS
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from utils.db_api.test import db
from loader import dp, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)

    await message.answer(f"Salom, {message.from_user.full_name}! 👋\n"
                         f"Orqa foni o'chirlishi kerak bo'lgan 🖼️ rasmni yuboring!")

    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)