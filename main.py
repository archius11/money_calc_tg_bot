from threading import Thread
from telegram_modules import bot_instance
from schedules.dyson import bg_task
import asyncio

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # daemon = Thread(target=bg_task, args=(loop,), daemon=True, name='Background')
    # daemon.start()

    bot_instance.run_polling()
