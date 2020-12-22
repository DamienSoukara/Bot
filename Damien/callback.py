#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ©️ @AmineSoukara

import pyrogram
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from config import Config
from config import Messages as tr
from translation import Translation
from .commands import start

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(c, callback_query):
    chat_id = callback_query.from_user.id
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    c.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = '➡️', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        url = "https://t.me/damienhelp"
        button = [
            [InlineKeyboardButton(text = '🔔 Updates Channel 🔔', url="https://t.me/DamienSoukara")],
            [InlineKeyboardButton(text = '📣 Support Chat 📣', url=url)],
            [InlineKeyboardButton(text = '⬅️', callback_data = f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '⬅️', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = '➡️', callback_data = f"help+{pos+1}")
            ],
        ]
    return button

@Client.on_callback_query()
async def cb_handler(c, m):
  cb_data = m.data

  if "home" in cb_data:
      button = [[
                InlineKeyboardButton("💬 Updates Channel", url="t.me/DamienSoukara"),
                InlineKeyboardButton("🗣 Support Group", url="t.me/damienhelp"),
                ],
                [
                InlineKeyboardButton("ℹ About", callback_data="about"),
                InlineKeyboardButton("🤔 Help", callback_data="morehelp")
                ],
                [InlineKeyboardButton("🤴 Developer 🤴", url="t.me/AmineSoukara")]]
      markup = InlineKeyboardMarkup(button)
      await c.edit_message_text(chat_id=m.message.chat.id,
                           message_id=m.message.message_id,
                           text=Translation.START_MSG.format(m.from_user.first_name),
                           reply_markup=markup)

  if "helpx" in cb_data:
        button = [[InlineKeyboardButton("🏠 Home", callback_data="home")]]
        markup = InlineKeyboardMarkup(button)
        await c.edit_message_text(chat_id=m.message.chat.id,
                           message_id=m.message.message_id,
                           text=Translation.HELP_USER.format(m.from_user.first_name),
                           disable_web_page_preview=True,
                           reply_markup=markup)

  if "ytdl" in cb_data:
        button = [[InlineKeyboardButton("🔙 Back", callback_data="morehelp"),
                InlineKeyboardButton("🏠 Home", callback_data="home")]]
        markup = InlineKeyboardMarkup(button)
        await c.edit_message_text(chat_id=m.message.chat.id,
                           message_id=m.message.message_id,
                           text=Translation.YTDL,
                           disable_web_page_preview=True,
                           reply_markup=markup)

  if "urldl" in cb_data:
        button = [[InlineKeyboardButton("🔙 Back", callback_data="morehelp"),
                InlineKeyboardButton("🏠 Home", callback_data="home")]]
        markup = InlineKeyboardMarkup(button)
        await c.edit_message_text(chat_id=m.message.chat.id,
                           message_id=m.message.message_id,
                           text=Translation.URLDL,
                           disable_web_page_preview=True,
                           reply_markup=markup)

  if "renamerx" in cb_data:
        button = [[InlineKeyboardButton("🔙 Back", callback_data="morehelp"),
                InlineKeyboardButton("🏠 Home", callback_data="home")]]
        markup = InlineKeyboardMarkup(button)
        await c.edit_message_text(chat_id=m.message.chat.id,
                           message_id=m.message.message_id,
                           text=Translation.RENAMERX,
                           disable_web_page_preview=True,
                           reply_markup=markup)

  if "morehelp" in cb_data:
        button = [[
                InlineKeyboardButton("🌐 Url Upload", callback_data="urldl"),
                InlineKeyboardButton("✍ Renamer", callback_data="renamerx"),
                ],
                [
                InlineKeyboardButton("🎞 YouTube DL", callback_data="ytdl"),
                InlineKeyboardButton("🤖 Feedback", url="t.me/DamienRobot")
                ],
                [InlineKeyboardButton("🏠 Home", callback_data="home")]]
        markup = InlineKeyboardMarkup(button)
        await c.edit_message_text(chat_id=m.message.chat.id,
                           message_id=m.message.message_id,
                           text=Translation.MOREHELP.format(m.from_user.first_name),
                           reply_markup=markup)

  if "about" in cb_data:
        button = [[InlineKeyboardButton("🏠 Home", callback_data="home")]]
        markup = InlineKeyboardMarkup(button)
        await c.edit_message_text(chat_id=m.message.chat.id,
                           message_id=m.message.message_id,
                           text=Translation.ABOUT.format(m.from_user.first_name),
                           disable_web_page_preview=True,
                           reply_markup=markup)
