from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .db import Model, get_or_create, db_session
from .user import User
from .history import History
from datetime import datetime


class Balance(Model):
    __tablename__ = 'balances'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User')
    balance = Column(Integer, default=0)

    def __lt__(self, other):
        return self.balance < other.balance

    @staticmethod
    def create_balance_move(user, amount, comment):
        current_balance_record = get_or_create(Balance, user=user)
        current_balance_record.balance += amount

        history = History(user=user, amount=amount, comment=comment)
        db_session.add(history)
        db_session.commit()



