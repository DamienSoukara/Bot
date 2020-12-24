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

@Client.on_callback_query()
async def cb_handler(c, m):
  cb_data = m.data

  if "home" in cb_data:
      button = [[
                InlineKeyboardButton("💬 My Channel", url="t.me/DamienSoukara"),
                InlineKeyboardButton("🗣 My Group", url="t.me/damienhelp"),
                ],
                [
                InlineKeyboardButton("ℹ About Me", callback_data="about"),
                InlineKeyboardButton("🌐 SocialMedia's", callback_data="sm")
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

  if "whtsp" in cb_data:
        button = [[InlineKeyboardButton("🔙 Back", callback_data="sm"),
                InlineKeyboardButton("🏠 Home", callback_data="home")]]
        markup = InlineKeyboardMarkup(button)
        await c.edit_message_text(chat_id=m.message.chat.id,
                           message_id=m.message.message_id,
                           text=Translation.WHTSP,
                           disable_web_page_preview=True,
                           reply_markup=markup)

  if "ig" in cb_data:
        button = [[InlineKeyboardButton("🔙 Back", callback_data="sm"),
                InlineKeyboardButton("🏠 Home", callback_data="home")]]
        markup = InlineKeyboardMarkup(button)
        await c.edit_message_text(chat_id=m.message.chat.id,
                           message_id=m.message.message_id,
                           text=Translation.IG,
                           disable_web_page_preview=True,
                           reply_markup=markup)

  if "fb" in cb_data:
        button = [[InlineKeyboardButton("🔙 Back", callback_data="sm"),
                InlineKeyboardButton("🏠 Home", callback_data="home")]]
        markup = InlineKeyboardMarkup(button)
        await c.edit_message_text(chat_id=m.message.chat.id,
                           message_id=m.message.message_id,
                           text=Translation.FB,
                           disable_web_page_preview=True,
                           reply_markup=markup)

  if "sm" in cb_data:
        button = [[
                InlineKeyboardButton("🌐 Facebook", callback_data="fb"),
                InlineKeyboardButton("🌐 Instagram", callback_data="ig"),
                ],
                [
                InlineKeyboardButton("🌐 WhatsApp", callback_data="whtsp"),
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
