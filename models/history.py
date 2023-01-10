from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .db import Model
from .user import User
from datetime import datetime


class History(Model):
    __tablename__ = 'history'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User')
    timestamp = Column(DateTime(), default=datetime.now)
    amount = Column(Integer, default=0)
    comment = Column(String, default='')
