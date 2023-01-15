from threading import Thread
from time import sleep
from datetime import datetime
from telegram_modules import bot_instance
from models import User
from .parse_dyson import parse_dyson


async def check_dysons():
    result = parse_dyson()
    if result:
        for user in User.query.all():
            await bot_instance.bot.send_message(chat_id=user.chat_id, text=result, disable_notification=False)
            for n in range(10):
                await bot_instance.bot.send_message(chat_id=user.chat_id, text='WARNING!!!!', disable_notification=False)
                sleep(1)


def bg_task(loop):

    while True:
        sleep(60)
        print(f'task {datetime.now()}')
        loop.create_task(check_dysons())
