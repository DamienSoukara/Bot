# Copyright (C) 2020 by AmineSoukara@Github, < https://github.com/AmineSoukara >.
# ©️ @AmineSoukara @DamienSoukara


from chatbase import Message
from config import Config
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def TRChatBase(chat_id, message_text, intent):
    msg = Message(api_key=Config.CHAT_BASE_TOKEN,
                  platform="Telegram",
                  version="1.3",
                  user_id=chat_id,
                  message=message_text,
                  intent=intent)
    msg.send()
