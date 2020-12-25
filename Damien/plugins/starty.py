import logging

from pyrogram import filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import Config
from Damien import bot
from help import Messages as tr
from helper_funcs.chat_base import TRChatBase
from translation import Translation

logging.basicConfig(level=logging.INFO)


@bot.on_message(filters.private)
async def sub(c, m: Message):
    if m.from_user.id in Config.BANNED_USERS:
        await m.reply_text("You are B A N N E D 🤣🤣🤣🤣 #Dev")
        return
    TRChatBase(m.from_user.id, m.text, "start")
    update_channel = Config.UPDATE_CHANNEL
    if update_channel:
        try:
            user = await c.get_chat_member(update_channel, m.chat.id)
            if user.status == "kicked":
                await m.reply_text("🤭 Sorry Dude, You are **B A N N E D** #Channel")
                return
        except UserNotParticipant:
            # await m.reply_text(f"Join @{update_channel} To Use Me")
            await m.reply_text(
                text="[●](https://i.imgur.com/t1JsZ0I.gif) **Join My Updates Channel To Mse Me : **",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="Subscribe", url=f"https://t.me/{update_channel}"
                            )
                        ]
                    ]
                ),
            )
            return
        except Exception:
            await m.reply_text("Something Wrong. Contact @AmineSoukara")
            return
