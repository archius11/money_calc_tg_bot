from abc import ABC
from telegram.ext.filters import MessageFilter
from enum import Enum
from models import User
from telegram_modules.utils import message_handler
from telegram_modules.users_instance import UsersInstance
from .menus import AddRecordSteps
from controllers.operations import add_record
from telegram_modules.buttons.main_menu import main_menu_buttons


class AddRecordBaseFilter(MessageFilter, ABC):
    def get_user(self, user_tg_id):
        return User.get_or_create(user_tg_id=user_tg_id)

    def filter(self, message):
        if message.text == '/cancel_operation':
            return False
        user_instances = UsersInstance()
        current_operation = user_instances.get_value(message.from_user, 'current_operation')
        user_stage = user_instances.get_value(message.from_user, 'stage')
        stage_name = AddRecordFilters(type(self))
        return current_operation == 'add_record' and user_stage.name == stage_name.name


@message_handler
class SelectUser(AddRecordBaseFilter):

    @staticmethod
    async def callback(update, context):
        db_user = User.get_or_none(name=update.effective_message.text)
        if not db_user:
            await context.bot.send_message(chat_id=update.effective_chat.id, text='invalid user')
            return

        user_instances = UsersInstance()
        user_instances.set_value(update.effective_user, 'stage', AddRecordSteps.AMOUNT)
        user_instances.set_value(update.effective_user, 'user', db_user)
        await context.bot.send_message(chat_id=update.effective_chat.id, text='enter amount')


@message_handler
class SetAmount(AddRecordBaseFilter):

    @staticmethod
    async def callback(update, context):
        if not update.effective_message.text.isdigit():
            await context.bot.send_message(chat_id=update.effective_chat.id, text='invalid amount')
            return
        amount = int(update.effective_message.text)
        user_instances = UsersInstance()
        user_instances.set_value(update.effective_user, 'stage', AddRecordSteps.COMMENT)
        user_instances.set_value(update.effective_user, 'amount', amount)
        await context.bot.send_message(chat_id=update.effective_chat.id, text='enter comment')


@message_handler
class SetComment(AddRecordBaseFilter):

    @staticmethod
    async def get_report_text(user, amount, comment):
        return f'{user} spent {amount}: {comment}'

    @staticmethod
    async def callback(update, context):
        user_instances = UsersInstance()
        user_instances.set_value(update.effective_user, 'comment', update.effective_message.text)
        user, amount, comment = user_instances.get_value(update.effective_user, 'user'),\
                               user_instances.get_value(update.effective_user, 'amount'),\
                               user_instances.get_value(update.effective_user, 'comment')
        add_record(user, amount, comment)
        report_text = await SetComment.get_report_text(user.name, amount, comment)
        user_instances.clear_instance(update.effective_user)
        # for user in User.query.all():
        #     await context.bot.send_message(chat_id=user.chat_id, text=report_text,
        #                                    reply_markup=main_menu_buttons(), disable_notification=True)


class AddRecordFilters(Enum):
    CHOOSE_USER = SelectUser
    AMOUNT = SetAmount
    COMMENT = SetComment
