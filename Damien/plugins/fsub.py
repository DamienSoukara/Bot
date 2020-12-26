# ©️ @AmineSoukara
# ©️ @DamienSoukara

import asyncio

from pyrogram import filters
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.types import (
    ChatPermissions,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from Damien import bot, cus_filters
from Damien.utils import check_bot_rights


@bot.on_message(filters.group & filters.new_chat_members & cus_filters.auth_chats)
async def _verify_msg_(_, msg: Message):
    """ Verify Msg for New chat Members """
    chat_id = msg.chat.id
    for member in msg.new_chat_members:
        try:
            user_status = (await msg.chat.get_member(member.id)).status
            if user_status in ("restricted", "kicked"):
                continue
        except Exception:
            pass
        if member.is_bot or not await check_bot_rights(chat_id, "can_restrict_members"):
            file_id, text, buttons = await wc_msg(member)
            reply = await msg.reply_animation(
                animation=file_id, caption=text, reply_markup=buttons
            )
            await asyncio.sleep(120)
            await reply.delete()
        else:
            await bot.restrict_chat_member(chat_id, member.id, ChatPermissions())
            try:
                await bot.get_chat_member("DamienSoukara", member.id)
            except UserNotParticipant:
                await force_sub(msg, member)
            else:
                await verify_keyboard(msg, member)
    msg.continue_propagation()


async def verify_keyboard(msg: Message, user):
    """ keyboard for verifying """
    _msg = f""" Hi {user.mention}, Welcome to {msg.chat.title}.
To Chat here, Please click on the button below. """
    button = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Verify Now 🤖",
                    callback_data=f"verify_cq({user.id} {msg.message_id})",
                )
            ]
        ]
    )
    await msg.reply_text(_msg, reply_markup=button)


async def force_sub(msg: Message, user):
    """ keyboard for force user to join channel """
    _msg = f""" Hi {user.mention}, Welcome to {msg.chat.title}.
Seems that you haven't join our Updates Channel.
__Click on Join Now and Unmute yourself.__ """
    button = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="💬 Join Now", url="https://t.me/DamienSoukara"
                ),
                InlineKeyboardButton(
                    text="🔕 Unmute Me",
                    callback_data=f"joined_unmute({user.id} {msg.message_id})",
                ),
            ]
        ]
    )
    await msg.reply_text(_msg, reply_markup=button)


async def wc_msg(user):
    """ arguments and reply_markup for sending after verify """
    gif = await bot.get_messages("DamienSoukara", 8)
    file_id = gif.animation.file_id
    text = f""" **Welcome** {user.mention},
__Check out the Button below. and feel free to ask here.__ 🤘 """
    buttons = InlineKeyboardMarkup(
        [[InlineKeyboardButton(text="📨 Feedback", url="https://t.me/DamienRobot")]]
    )
    return file_id, text, buttons
