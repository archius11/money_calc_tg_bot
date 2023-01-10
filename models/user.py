from sqlalchemy import Column, Integer, String
from .db import Model, get_or_create, get_or_none


class User(Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer, unique=True)
    name = Column(String, unique=True)

    @staticmethod
    def get_or_create(**kwargs):
        return get_or_create(User, **kwargs)

    @staticmethod
    def get_or_none(**kwargs):
        return get_or_none(User, **kwargs)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name