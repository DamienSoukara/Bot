import asyncio
import logging
from pyrogram import filters
from pyrogram.types import (
    Message, ChatPermissions, CallbackQuery,
    InlineKeyboardMarkup, InlineKeyboardButton)
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram import Client

from Damien import cus_filters
from Damien.utils import check_bot_rights

@Client.on_message(
    filters.group & filters.new_chat_members & cus_filters.auth_chats)
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
            file_id, file_ref, text, buttons = await wc_msg(member)
            reply = await msg.reply_animation(
                animation=file_id, file_ref=file_ref,
                caption=text, reply_markup=buttons
            )
            await asyncio.sleep(120)
            await reply.delete()
        else:
            await Client.restrict_chat_member(chat_id, member.id, ChatPermissions())
            try:
                await Client.get_chat_member("DamienSoukara", member.id)
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
                    text="Verify now 🤖",
                    callback_data=f"verify_cq({user.id} {msg.message_id})")
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
                    text="Join Now",
                    url="https://t.me/DamienSoukara"),
                InlineKeyboardButton(
                    text="Unmute Me",
                    callback_data=f"joined_unmute({user.id} {msg.message_id})")
            ]
        ]
    )
    await msg.reply_text(_msg, reply_markup=button)


async def wc_msg(user):
    """ arguments and reply_markup for sending after verify """
    gif = await Client.get_messages("damienhelp", 25293)
    file_id = gif.animation.file_id
    file_ref = gif.animation.file_ref
    text = f""" **Welcome** {user.mention},
__Check out the Button below. and feel free to ask here.__ 🤘 """
    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="More info.",
                    url="https://t.me/DamienSoukara/637843"
                )
            ]
        ]
    )
    return file_id, file_ref, text, buttons


@Client.on_callback_query(filters.regex(pattern=r"verify_cq\((.+?)\)"))
async def _verify_user_(_, c_q: CallbackQuery):
    _a, _b = c_q.matches[0].group(1).split(' ', maxsplit=1)
    user_id = int(_a)
    msg_id = int(_b)
    if c_q.from_user.id == user_id:
        await c_q.message.delete()
        await Client.unban_chat_member(c_q.message.chat.id, user_id)
        file_id, file_ref, text, buttons = await wc_msg(await Client.get_users(user_id))
        msg = await Client.send_animation(
            c_q.message.chat.id,
            animation=file_id,
            file_ref=file_ref,
            caption=text, reply_markup=buttons,
            reply_to_message_id=msg_id
        )
        await asyncio.sleep(120)
        await msg.delete()
    else:
        await c_q.answer("This message is not for you. 😐", show_alert=True)


@Client.on_callback_query(filters.regex(pattern=r"joined_unmute\((.+?)\)"))
async def _on_joined_unmute_(_, c_q: CallbackQuery):
    if not c_q.message.chat:
        return
    _a, _b = c_q.matches[0].group(1).split(' ', maxsplit=1)
    user_id = int(_a)
    msg_id = int(_b)
    bot_id = (await Client.get_me()).id
    chat_id = c_q.message.chat.id

    user = await Client.get_users(user_id)

    if c_q.from_user.id == user_id:
        get_user = await Client.get_chat_member(chat_id, user_id)
        if get_user.restricted_by and get_user.restricted_by.id == bot_id:
            try:
                await Client.get_chat_member("DamienSoukara", user_id)
            except UserNotParticipant:
                await c_q.answer(
                    "Click on Join Now button to Join our Updates Channel"
                    " and click on Unmute me Button again.", show_alert=True)
            else:
                await c_q.message.delete()
                await Client.unban_chat_member(c_q.message.chat.id, user_id)
                f_d, f_r, txt, btns = await wc_msg(user)
                msg = await Client.send_animation(
                    c_q.message.chat.id,
                    animation=f_d,
                    file_ref=f_r,
                    caption=txt, reply_markup=btns,
                    reply_to_message_id=msg_id
                )
                await asyncio.sleep(120)
                await msg.delete()
        else:
            await c_q.answer(
                "Admins Muted you for another reason, I Can't unmute you.",
                show_alert=True)
    else:
        await c_q.answer(
            f"This Message is Only for {user.first_name}", show_alert=True)
