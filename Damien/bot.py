__all__ = ["bot", "START_TIME"]

import time

from pyrogram import Client

from . import Config, logging

_LOG = logging.getLogger(__name__)
START_TIME = time.time()

plugins = dict(root="Damien.plugins")
bot = Client(
     'Damien Soukara',
      bot_token = Config.BOT_TOKEN,
      api_id = Config.APP_ID,
      api_hash = Config.API_HASH,
      plugins = plugins
)

_LOG.info("assistant-bot initialized!")
