## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgBiXZhoXymAGvW5Xm4X5Btm2MKdropz82vnh4P0N1tkfnctzQeFoax1yHspGzs-LNP6Urgs6l7at2rUZbwjZhQaNo30vLiY10V3diuPerBgNN9ceOHKldcSa2JtSXG27bIxq3AET29K-0sTH2AkVPK1BdeO2OisE6eoJIjVxZnnKCXpyzduHhmNuvptlQg09dWjSKo9aqJiwBzMxh8-3o-cGvDF6o1mu1uwxrlAuuYg-3Q4MTzvmSUjhKMbHarisD9ims0P3_ZhNDG9-as5tEA0D5TNN6hxV9Wa54wnquHxKromzrFKOPHAYAOHUTIjkegAYYBATPRqfAZUU_pt-0OWAAAAATc7scYA")
BOT_TOKEN = getenv("BOT_TOKEN", "5360553244:AAGmOmstlrMeF7EpcUicEuMvQ_ATacPB0Kw")
BOT_NAME = getenv("BOT_NAME", "- ꧑ᥙ᥉Ꭵᥴ ℮᥊ﾋꪜᥲ .")
API_ID = int(getenv("API_ID", "9377181"))
API_HASH = getenv("API_HASH", "b881d85aa4012e6ae4875f79e666ecf1")
OWNER_NAME = getenv("OWNER_NAME", "ყ᥆ᥙ᥉Ꭵƒ")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Yzys5")
ALIVE_NAME = getenv("ALIVE_NAME", "ყ᥆ᥙ᥉Ꭵƒ")
BOT_USERNAME = getenv("BOT_USERNAME", "ISISIPI_bot")
OWNER_ID = getenv("OWNER_ID", "1734502126")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ISISIPI")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "C_H_H_C")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "C_H_H_C")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://l.top4top.io/p_2363dcjiw1.jpg")
START_PIC = getenv("START_PIC", "https://l.top4top.io/p_2363dcjiw1.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
