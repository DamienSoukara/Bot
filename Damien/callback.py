#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ©️ @AmineSoukara

import pyrogram
from pyrogram import filters
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from config import Config
from translation import Translation
from .commands import start

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
                InlineKeyboardButton("🤔 Help", callback_data="helpx")
                ],
                [InlineKeyboardButton("🤴 Developer 🤴", url="t.me/AmineSoukara")]]
      markup = InlineKeyboardMarkup(button)
      await m.message.delete()
      await c.send_message(chat_id=m.message.chat.id,
                           text=Translation.START_MSG.format(m.from_user.first_name),
                           reply_markup=markup)

  if "feed" in cb_data:
      Config.Client.append(m.from_user.id)
      button = [[InlineKeyboardButton("❌ Cancel", callback_data="cancel")]]
      markup = InlineKeyboardMarkup(button)
      await m.message.delete()
      await c.send_message(chat_id=m.message.chat.id, text="💬 Send Your FeedBack Here I Will Notify The Admin.", reply_markup=markup)

  if "helpx" in cb_data:
      button = [[InlineKeyboardButton("🏠 Home", callback_data="home")]]
      markup = InlineKeyboardMarkup(button)
      await m.message.delete()
      await c.send_message(chat_id=m.message.chat.id,
                           text=Translation.HELP_USER.format(m.from_user.first_name),
                           disable_web_page_preview=True,
                           reply_markup=markup)

  if "about" in cb_data:
      button = [[InlineKeyboardButton("🏠 Home", callback_data="home")]]
      markup = InlineKeyboardMarkup(button)
      await m.message.delete()
      await c.send_message(chat_id=m.message.chat.id,
                           text=Translation.ABOUT.format(m.from_user.first_name),
                           disable_web_page_preview=True,
                           reply_markup=markup)
