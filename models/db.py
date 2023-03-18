from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, String

db_engine = create_engine('sqlite:////home/db/main.db', echo=True, future=True)
db_session = scoped_session(sessionmaker(autocommit=True,
                                         autoflush=True,
                                         bind=db_engine))

Model = declarative_base()
Model.query = db_session.query_property()

def init_db():
    from .user import User
    from .history import History
    from .balances import Balance
    Model.metadata.create_all(bind=db_engine)

    def add_column(engine, table_name, column):
        column_name = column.compile(dialect=engine.dialect)
        column_type = column.type.compile(engine.dialect)
        with engine.connect() as conn:
            with conn.begin():  # Optional: start a transaction
                conn.execute(text('ALTER TABLE %s ADD COLUMN %s %s' % (table_name, column_name, column_type)))

    # column = Column('chat_id', String)
    # add_column(db_engine, 'users', column)


def get_or_create(model, **kwargs):
    instance = db_session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        db_session.add(instance)
        db_session.commit()
        return instance


def get_or_none(model, **kwargs):
    instance = db_session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        return None
