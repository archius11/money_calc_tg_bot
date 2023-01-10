from telegram import KeyboardButton, ReplyKeyboardMarkup
from enum import Enum
from models import User
from telegram_modules.buttons import Buttons
from telegram_modules.buttons.main_menu import cancel_menu_buttons


class AddRecordSteps(Enum):
    CHOOSE_USER = 1
    AMOUNT = 2
    COMMENT = 3


def add_record_menu_1():
    users = [user.name for user in User.query.all()]
    button_list = [KeyboardButton(user) for user in users]
    button_list += cancel_menu_buttons()
    return ReplyKeyboardMarkup(Buttons.build_menu(button_list, n_cols=2), resize_keyboard=True)
