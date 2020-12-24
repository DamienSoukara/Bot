#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ©️ @AmineSoukara

import asyncio

from pyrogram import filters
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from Damien import bot
from translation import Translation

from .fsub import wc_msg, force_sub, verify_keyboard


@bot.on_callback_query(filters.regex(pattern=r"verify_cq\((.+?)\)"))
async def _verify_user_(_, c_q: CallbackQuery):
    _a, _b = c_q.matches[0].group(1).split(" ", maxsplit=1)
    user_id = int(_a)
    msg_id = int(_b)
    if c_q.from_user.id == user_id:
        await c_q.message.delete()
        await bot.unban_chat_member(c_q.message.chat.id, user_id)
        file_id, text, buttons = await wc_msg(await bot.get_users(user_id))
        msg = await bot.send_animation(
            c_q.message.chat.id,
            animation=file_id,
            caption=text,
            reply_markup=buttons,
            reply_to_message_id=msg_id,
        )
        await asyncio.sleep(120)
        await msg.delete()
    else:
        await c_q.answer("This message is not for you. 😐", show_alert=True)


@bot.on_callback_query(filters.regex(pattern=r"joined_unmute\((.+?)\)"))
async def _on_joined_unmute_(_, c_q: CallbackQuery):
    if not c_q.message.chat:
        return
    _a, _b = c_q.matches[0].group(1).split(" ", maxsplit=1)
    user_id = int(_a)
    msg_id = int(_b)
    bot_id = (await bot.get_me()).id
    chat_id = c_q.message.chat.id

    user = await bot.get_users(user_id)

    if c_q.from_user.id == user_id:
        get_user = await bot.get_chat_member(chat_id, user_id)
        if get_user.restricted_by and get_user.restricted_by.id == bot_id:
            try:
                await bot.get_chat_member("DamienSoukara", user_id)
            except UserNotParticipant:
                await c_q.answer(
                    "Click on Join Now button to Join our Updates Channel"
                    " and click on Unmute me Button again.",
                    show_alert=True,
                )
            else:
                await c_q.message.delete()
                await bot.unban_chat_member(c_q.message.chat.id, user_id)
                f_d, txt, btns = await wc_msg(user)
                msg = await bot.send_animation(
                    c_q.message.chat.id,
                    animation=f_d,
                    caption=txt,
                    reply_markup=btns,
                    reply_to_message_id=msg_id,
                )
                await asyncio.sleep(120)
                await msg.delete()
        else:
            await c_q.answer(
                "Admins Muted you for another reason, I Can't unmute you.",
                show_alert=True,
            )
    else:
        await c_q.answer(f"This Message is Only for {user.first_name}", show_alert=True)


@bot.on_callback_query()
async def cb_handler(c, m):
    cb_data = m.data

    if "home" in cb_data:
        button = [
            [
                InlineKeyboardButton("💬 My Channel", url="t.me/DamienSoukara"),
                InlineKeyboardButton("🗣 My Group", url="t.me/damienhelp"),
            ],
            [
                InlineKeyboardButton("ℹ About Me", callback_data="about"),
                InlineKeyboardButton("🌐 SocialMedia's", callback_data="sm"),
            ],
            [InlineKeyboardButton("🤴 Developer 🤴", url="t.me/AmineSoukara")],
        ]
        markup = InlineKeyboardMarkup(button)
        await c.edit_message_text(
            chat_id=m.message.chat.id,
            message_id=m.message.message_id,
            text=Translation.START_MSG.format(m.from_user.first_name),
            reply_markup=markup,
        )

    if "helpx" in cb_data:
        button = [[InlineKeyboardButton("🏠 Home", callback_data="home")]]
        markup = InlineKeyboardMarkup(button)
        await c.edit_message_text(
            chat_id=m.message.chat.id,
            message_id=m.message.message_id,
            text=Translation.HELP_USER.format(m.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=markup,
        )

    if "whtsp" in cb_data:
        button = [
            [
                InlineKeyboardButton("🔙 Back", callback_data="sm"),
                InlineKeyboardButton("🏠 Home", callback_data="home"),
            ]
        ]
        markup = InlineKeyboardMarkup(button)
        await c.edit_message_text(
            chat_id=m.message.chat.id,
            message_id=m.message.message_id,
            text=Translation.WHTSP,
            disable_web_page_preview=True,
            reply_markup=markup,
        )

    if "ig" in cb_data:
        button = [
            [
                InlineKeyboardButton("🔙 Back", callback_data="sm"),
                InlineKeyboardButton("🏠 Home", callback_data="home"),
            ]
        ]
        markup = InlineKeyboardMarkup(button)
        await c.edit_message_text(
            chat_id=m.message.chat.id,
            message_id=m.message.message_id,
            text=Translation.IG,
            disable_web_page_preview=True,
            reply_markup=markup,
        )

    if "fb" in cb_data:
        button = [
            [
                InlineKeyboardButton("🔙 Back", callback_data="sm"),
                InlineKeyboardButton("🏠 Home", callback_data="home"),
            ]
        ]
        markup = InlineKeyboardMarkup(button)
        await c.edit_message_text(
            chat_id=m.message.chat.id,
            message_id=m.message.message_id,
            text=Translation.FB,
            disable_web_page_preview=True,
            reply_markup=markup,
        )

    if "sm" in cb_data:
        button = [
            [
                InlineKeyboardButton("🌐 Facebook", callback_data="fb"),
                InlineKeyboardButton("🌐 Instagram", callback_data="ig"),
            ],
            [
                InlineKeyboardButton("🌐 WhatsApp", callback_data="whtsp"),
                InlineKeyboardButton("🤖 Feedback", url="t.me/DamienRobot"),
            ],
            [InlineKeyboardButton("🏠 Home", callback_data="home")],
        ]
        markup = InlineKeyboardMarkup(button)
        await c.edit_message_text(
            chat_id=m.message.chat.id,
            message_id=m.message.message_id,
            text=Translation.MOREHELP.format(m.from_user.first_name),
            reply_markup=markup,
        )

    if "about" in cb_data:
        button = [[InlineKeyboardButton("🏠 Home", callback_data="home")]]
        markup = InlineKeyboardMarkup(button)
        await c.edit_message_text(
            chat_id=m.message.chat.id,
            message_id=m.message.message_id,
            text=Translation.ABOUT.format(m.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=markup,
        )
