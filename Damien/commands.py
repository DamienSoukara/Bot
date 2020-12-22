import logging
from config import Messages as tr
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from translation import Translation
logging.basicConfig(level=logging.INFO)

@Client.on_message(filters.private & filters.incoming & filters.command(['startt']))
def _startt(c, m):
    c.send_message(m.chat.id,
        text=tr.X_MSG.format(m.from_user.first_name, m.from_user.id),
        parse_mode="markdown",
        reply_to_message_id=m.message_id
        )

@Client.on_message(filters.command(["start"]))
async def start(c, m):
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
      await c.send_message(chat_id=m.chat.id,
                           text=Translation.START_MSG.format(m.from_user.first_name),
                           reply_to_message_id=m.message_id,
                           reply_markup=markup)

@Client.on_message(filters.private & filters.command('about'))
def _about(c, m):
    chatID = m.chat.id
    photoUrl = "https://telegra.ph/file/aa59c3024666f7bc9f712.jpg"
    c.send_photo(chatID, photoUrl, 
    parse_mode = "markdown", 
    caption = "**Hellooooo**", 
    reply_to_message_id = m.message_id, 
    reply_markup = InlineKeyboardMarkup(
                    [[InlineKeyboardButton("👑 My Owner", url=f"t.me/AmineSoukara"),
                    InlineKeyboardButton("💬 Channel", url="t.me/DamienSoukara")],
                    [InlineKeyboardButton("🔥  DAMIEN-X", callback_data="about")
                    ]]
                )
            )

@Client.on_message(filters.private & filters.command('test'))
def _test(c, m):
    chatID = m.chat.id # ايدي المحادثة
    photoUrl = "https://i.imgur.com/5Fw6nMR.jpg" # ايدي الصورة 
    c.send_photo(chatID, photoUrl, caption = "**Damien**", parse_mode="markdown")

@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_notification = True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
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
