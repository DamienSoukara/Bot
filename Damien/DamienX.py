import logging
from DamienConfig import Messages as tr
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
logging.basicConfig(level=logging.INFO)

@Client.on_message(filters.private & filters.incoming & filters.command(['start']))
def _start(client, message):
    client.send_message(message.chat.id,
        text=tr.X_MSG.format(message.from_user.first_name, message.from_user.id),
        parse_mode="markdown",
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.private & filters.command('about'))
def _about(client, message):
    chatID = message.chat.id
    photoUrl = "https://telegra.ph/file/aa59c3024666f7bc9f712.jpg"
    client.send_photo(chatID, photoUrl, 
    parse_mode = "markdown", 
    caption = "**Hellooooo**", 
    reply_to_message_id = message.message_id, 
    reply_markup = InlineKeyboardMarkup(
                    [[InlineKeyboardButton("👑 My Owner", url=f"t.me/AmineSoukara"),
                    InlineKeyboardButton("💬 Channel", url="t.me/DamienSoukara")],
                    [InlineKeyboardButton("🔥  DAMIEN-X", callback_data="about")
                    ]]
                )
            )

@Client.on_message(filters.private & filters.command('test'))
def _test(client, message):
    chatID = message.chat.id # ايدي المحادثة
    photoUrl = "https://i.imgur.com/5Fw6nMR.jpg" # ايدي الصورة 
    client.send_photo(chatID, photoUrl, caption = "**Damien**", parse_mode="markdown")

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
@Client.on_callback_query()
async def cb_handler(c, m):
  cb_data = m.data

  if "feed" in cb_data:
      Config.feedback.append(m.from_user.id)
      button = [[InlineKeyboardButton("❌ Cancel", callback_data="cancel")]]
      markup = InlineKeyboardMarkup(button)
      await m.message.delete()
      await c.send_message(chat_id=m.message.chat.id, text="💬 Send Your FeedBack Here I Will Notify The Admin.", reply_markup=markup)

  if "cancel" in cb_data:
      if m.from_user.id in Config.feedback:
         Config.feedback.remove(m.from_user.id)
      if m.from_user.id in Config.LOGIN:
         Config.LOGIN.remove(m.from_user.id)
      await m.message.delete()
      await start(c, m.message)

  if "rules" in cb_data:
      await m.message.delete()
      await c.send_message(chat_id=m.message.chat.id, text=Translation.RULES)

  if "reply" in cb_data:
      id = m.data.split("+")[1]
      Config.SEND.append(id)
      await c.send_message(chat_id=m.message.chat.id, text="💬 Reply Me, The Text Which You Wanted To Send")

  if "about" in cb_data:
      await m.message.delete()
      await c.send_message(chat_id=m.message.chat.id, text="ABOUT", disable_web_page_preview=True)
