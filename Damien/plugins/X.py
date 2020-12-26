from pyrogram import Client, __version__, emoji
from pyrogram.types import InlineQuery

from config import Config
from Damien.utils import docs

NEXT_OFFSET = 25
CACHE_TIME = 5

FIRE_THUMB = "https://i.imgur.com/qhYYqZa.png"
ROCKET_THUMB = "https://i.imgur.com/PDaYHd8.png"
OPEN_BOOK_THUMB = "https://i.imgur.com/v1XSJ1D.png"
SCROLL_THUMB = "https://i.imgur.com/L1u0VlX.png"

VERSION = __version__.split("-")[0]


@Client.on_inline_query()
async def inline(_, query: InlineQuery):
    string = query.query.lower()

    if query.from_user.id in Config.BANNED_USERS:
        pass
    if string == "":
        await query.answer(
            results=docs.BAN_RESULTS,
            cache_time=CACHE_TIME,
            switch_pm_text=f"{emoji.MAGNIFYING_GLASS_TILTED_RIGHT} Banned",
            switch_pm_parameter="start",
        )

        return

    int(query.offset or 0)
    f"{emoji.OPEN_BOOK} Pyrogram Docs"
