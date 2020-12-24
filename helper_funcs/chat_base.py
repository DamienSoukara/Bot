#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ©️ @AmineSoukara.

# the logging things
from chatbase import Message
import os
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"


# the Telegram trackings


def TRChatBase(chat_id, message_text, intent):
    msg = Message(api_key=Config.CHAT_BASE_TOKEN,
                  platform="Telegram",
                  version="1.3",
                  user_id=chat_id,
                  message=message_text,
                  intent=intent)
    msg.send()
