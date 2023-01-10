from telegram.ext import Application
from config import BOT_TOKEN

bot_instance = Application.builder().token(BOT_TOKEN).build()
print(f'new app {id(bot_instance)}')

from telegram_modules import app_cmds

from models.db import init_db
init_db()