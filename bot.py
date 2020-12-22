import logging
from pyrogram import Client
from config import Config

logging.basicConfig(level=logging.INFO)

plugins = dict(
    root="Damien",
    include=[
        "DamienX"
    ]
)

app = Client(
     'Damien Soukara',
      bot_token = Config.BOT_TOKEN,
      api_id = Config.APP_ID,
      api_hash = Config.API_HASH,
      plugins = plugins
)

app.run()
