#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ©️ @AmineSoukara

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)
from helper_funcs.chat_base import TRChatBase
from pyrogram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from translation import Translation
from .commands import start

@pyrogram.Client.on_callback_query()
async def cb_handler(c, m):
  cb_data = m.data

    if "helpx" in cb_data:
        button = [[InlineKeyboardButton("🏠 Home", callback_data="home")]]
        markup = InlineKeyboardMarkup(button)
        await bot.edit_message_text(chat_id=update.message.chat.id,
                           message_id=update.message.message_id,
                           text=Translation.HELP_USER.format(update.from_user.first_name),
                           disable_web_page_preview=True,
                           reply_markup=markup)

    if "ytdl" in cb_data:
        button = [[InlineKeyboardButton("🔙 Back", callback_data="morehelp"),
                InlineKeyboardButton("🏠 Home", callback_data="home")]]
        markup = InlineKeyboardMarkup(button)
        await bot.edit_message_text(chat_id=update.message.chat.id,
                           message_id=update.message.message_id,
                           text=Translation.YTDL,
                           disable_web_page_preview=True,
                           reply_markup=markup)

    if "urldl" in cb_data:
        button = [[InlineKeyboardButton("🔙 Back", callback_data="morehelp"),
                InlineKeyboardButton("🏠 Home", callback_data="home")]]
        markup = InlineKeyboardMarkup(button)
        await bot.edit_message_text(chat_id=update.message.chat.id,
                           message_id=update.message.message_id,
                           text=Translation.URLDL,
                           disable_web_page_preview=True,
                           reply_markup=markup)

    if "renamerx" in cb_data:
        button = [[InlineKeyboardButton("🔙 Back", callback_data="morehelp"),
                InlineKeyboardButton("🏠 Home", callback_data="home")]]
        markup = InlineKeyboardMarkup(button)
        await bot.edit_message_text(chat_id=update.message.chat.id,
                           message_id=update.message.message_id,
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
        await bot.edit_message_text(chat_id=update.message.chat.id,
                           message_id=update.message.message_id,
                           text=Translation.MOREHELP.format(update.from_user.first_name),
                           reply_markup=markup)

    if "about" in cb_data:
        button = [[InlineKeyboardButton("🏠 Home", callback_data="home")]]
        markup = InlineKeyboardMarkup(button)
        await bot.edit_message_text(chat_id=update.message.chat.id,
                           message_id=update.message.message_id,
                           text=Translation.ABOUT.format(update.from_user.first_name),
                           disable_web_page_preview=True,
                           reply_markup=markup)

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
      await bot.edit_message_text(chat_id=update.message.chat.id,
                           message_id=update.message.message_id,
                           text=Translation.START_MSG.format(update.from_user.first_name),
                           reply_markup=markup)
