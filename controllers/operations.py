
from models import User, Balance
from models.db import db_session


def add_record(user, amount, comment):
    with db_session() as session:
        Balance.create_balance_move(user, amount, comment)
        session.commit()


def get_total_balance():
    balances = sorted(Balance.query.all(), reverse=True)

    balances_dicts = [{
                        'user': obj.user,
                        'balance': obj.balance
                        } for obj in balances]

    if len(balances)>1:
        second_balance = balances[1].balance
    else:
        second_balance = balances[0].balance

    for balance in balances_dicts:
        balance['balance'] -= second_balance

    return balances_dicts


def create_user(name, tg_id):
    user = User.get_or_create(name=name, tg_id=tg_id)
