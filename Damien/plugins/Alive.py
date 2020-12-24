import random
import time

from pyrogram import filters
from pyrogram.errors.exceptions import FileIdInvalid, FileReferenceEmpty
from pyrogram.errors.exceptions.bad_request_400 import BadRequest
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from Damien import bot, cus_filters, versions
from Damien.bot import START_TIME
from Damien.utils import time_formatter

LOGO_DATA = []
MSG_IDS = [25375, 25340, 25369]


@bot.on_message(filters.command("alive") & cus_filters.auth_chats)
async def _alive(_, message: Message):
    try:
        await _sendit(message.chat.id)
    except (FileIdInvalid, FileReferenceEmpty, BadRequest):
        await _refresh_data()
        await _sendit(message.chat.id)


async def _refresh_data():
    LOGO_DATA.clear()
    for msg in await bot.get_messages("DamienHelp", MSG_IDS):
        if not msg.animation:
            continue
        gif = msg.animation
        LOGO_DATA.append((gif.file_id))


async def _sendit(chat_id):
    if not LOGO_DATA:
        await _refresh_data()
    caption = f"""
**🤖 Bot Uptime** : `{time_formatter(time.time() - START_TIME)}`
**🤖 Bot Version** : `{versions.__assistant_version__}`
**️️⭐ Python** : `{versions.__python_version__}`
**💥 Pyrogram** : `{versions.__pyro_version__}` """
    button = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="License",
                    url=(
                        "https://github.com/"
                        "AmineSoukara"
                    ),
                ),
                InlineKeyboardButton(
                    text="Repo", url="https://github.com/"
                ),
            ]
        ]
    )
    file_id = random.choice(LOGO_DATA)
    await bot.send_animation(
        chat_id=chat_id,
        animation=file_id,
        caption=caption,
        reply_markup=button,
    )
