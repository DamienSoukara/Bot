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
    BOT_TOKEN = "1407670019:AAH2ib084959Rla9zbYVnhecIQl0CBR1zL8"
    APP_ID = "1250763"
    API_HASH = "11d05c637abdb46e35f51bc73241c75c"
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


