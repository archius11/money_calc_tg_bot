
from controllers.operations import get_total_balance, create_user
from .utils import command_handler
from .add_record import AddRecordSteps, add_record_menu_1
from .users_instance import UsersInstance
from telegram_modules.buttons.main_menu import main_menu_buttons


@command_handler("start")
async def start(update, context):
    user = update.effective_user
    create_user(user.first_name, user.id, update.effective_chat.id)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Select operation",
                                   reply_markup=main_menu_buttons())


@command_handler("cancel_operation")
async def cancel_operation(update, context):
    user_instances = UsersInstance()
    user_instances.clear_instance(update.effective_user)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='operation cancelled',
                                   reply_markup=main_menu_buttons())


@command_handler("balance")
async def tg_print_balance(update, context):
    balance = get_total_balance()
    msg = '\n'.join([f'{user["user"]}: {user["balance"]}' for user in balance])
    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)


@command_handler("add_record")
async def tg_add_record(update, context):
    user_instances = UsersInstance()
    user_instances.set_value(update.effective_user, 'current_operation', 'add_record')
    user_instances.set_value(update.effective_user, 'stage', AddRecordSteps.CHOOSE_USER)

    await context.bot.send_message(chat_id=update.effective_chat.id, text='select user', reply_markup=add_record_menu_1())
