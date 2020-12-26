# Copyright (C) 2020 by AmineSoukara@Github, < https://github.com/AmineSoukara >.
# ©️ @AmineSoukara @DamienSoukara

import os

from dotenv import load_dotenv

if os.path.isfile("config.env"):
    load_dotenv("config.env")


class Config:
    """ assistant configs """
    APP_ID = int(os.environ.get("APP_ID", 0))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    CHAT_BASE_TOKEN = os.environ.get("CHAT_BASE_TOKEN", "")
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
    BANNED_USERS = set(
        int(x) for x in os.environ.get(
            "BANNED_USERS", "").split())
    AUTH_CHATS = set([-1001474594528])  # @DamienHelp
    if os.environ.get("AUTH_CHATS"):
        AUTH_CHATS.update(map(int, os.environ.get("AUTH_CHATS").split()))
    WHITELIST_CHATS = set([-1001366299402])  # @Private
    if os.environ.get("WHITELIST_CHATS"):
        WHITELIST_CHATS.update(
            map(int, os.environ.get("WHITELIST_CHATS").split()))
    DEV_USERS = (
        853393439,  # @AmineSoukara
        1294768559  # @NagatoDamien
    )
    ADMINS = {}
    MAX_MSG_LENGTH = 4096


class Messages():
    HELP_MSG = [
        ".",
        "**Hello 🌍 World**",
        "Another Text 😅",
        "**[👨‍💻](https://i.imgur.com/TaOKIkf.gif) Developed By : @AmineSoukara**"]

    X_MSG = "Hey! [👋](https://i.imgur.com/Ljhp9Kk.gif) [{}](tg://user?id={}) \n©️ Read /help & /about"

    ABOUT_MSG = "©️ https://t.me/DamienSoukara"

    START = "HI BABY"
