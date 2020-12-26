# Copyright (C) 2020 by AmineSoukara@Github, < https://github.com/AmineSoukara >.
# ©️ @AmineSoukara @DamienSoukara

__all__ = ["logging"]

import logging

# enable logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logging.getLogger("pyrogram").setLevel(logging.WARNING)
