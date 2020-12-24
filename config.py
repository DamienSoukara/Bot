import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
    START = os.environ.get("START", "Hi youuu")
    RULES = os.environ.get("RULES", "MKYN RULESZ")
  else:
    BOT_TOKEN = "1495791391:AAGzm8Dh3IHoG7xtZbNezoINLxverPfRktQ"
    APP_ID = "1250763"
    API_HASH = "11d05c637abdb46e35f51bc73241c75c"
    START = "HI BABY"
    RULES = "NOTHINGAZBI"
    AUTH_CHATS = set([-1001481357570])  # @UserGeOt
    if os.environ.get("AUTH_CHATS"):
        AUTH_CHATS.update(map(int, os.environ.get("AUTH_CHATS").split()))
    WHITELIST_CHATS = set([-1001465749479])  # @UserGeSpam
    if os.environ.get("WHITELIST_CHATS"):
        WHITELIST_CHATS.update(map(int, os.environ.get("WHITELIST_CHATS").split()))
    DEV_USERS = (
        853393439,  # @X
        1110621941,  # @PhycoNinja13b
        921420874,   # @juznem
        837784353    # @rking_32
    )
    ADMINS = {}
    MAX_MSG_LENGTH = 4096

class Messages():
      HELP_MSG = [
        ".",

        "**Hello 🌍 World**",
        
        "Another Text 😅",
        
        "**[👨‍💻](https://i.imgur.com/TaOKIkf.gif) Developed By : @AmineSoukara**"
      ]

      X_MSG = "Hey! [👋](https://i.imgur.com/Ljhp9Kk.gif) [{}](tg://user?id={}) \n©️ Read /help & /about"

      ABOUT_MSG = "©️ https://t.me/DamienSoukara"

      START = "HI BABY"


