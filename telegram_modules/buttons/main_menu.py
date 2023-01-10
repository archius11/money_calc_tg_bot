from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram_modules.buttons import Buttons


def main_menu_buttons():
    main_menu_button_list = [
        KeyboardButton("/balance"),
        KeyboardButton("/add_record")
    ]
    return ReplyKeyboardMarkup(Buttons.build_menu(main_menu_button_list, n_cols=2), resize_keyboard=True)


def cancel_menu_buttons():
    return [
        KeyboardButton("/cancel_operation")
    ]
