import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
    START = os.environ.get("START", "Hi youuu")
    RULES = os.environ.get("RULES", "MKYN RULESZ)
  else:
    BOT_TOKEN = "1236676824:AAHBjEYEf5M5jk5rfrZ7qShepqNS4nFbR5s"
    APP_ID = "1358970"
    API_HASH = "57aff1848504fcde424d181d5cfee983"
    START = "HI BABY"
    RULES = "NOTHINGAZBI"

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


