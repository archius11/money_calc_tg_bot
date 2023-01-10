from telegram.ext import CommandHandler, MessageHandler
from telegram_modules import bot_instance


def command_handler(command):
    def decorator(func):
        handler = CommandHandler(command, func)
        bot_instance.add_handler(handler)
        return func
    return decorator


def message_handler(filter_class):
    my_filter = filter_class()
    my_handler = MessageHandler(my_filter, filter_class.callback)
    bot_instance.add_handler(my_handler)
    return filter_class
