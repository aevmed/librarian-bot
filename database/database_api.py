import datetime

from sqlalchemy import create_engine, Column, Integer, Text, BigInteger, Float
from sqlalchemy.orm import declarative_base, Session

now_date = datetime.datetime.now()
now_date = now_date.strftime('%Y-%m-%d %H:%M:%S')

engine = create_engine('postgresql://postgres:postgres@localhost:5432/bot')

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(BigInteger)
    username = Column(Text)
    date = Column(Text)


class Books(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_name = Column(Text)
    book_author = Column(Text)
    book_description = Column(Text)
    book_owner = Column(BigInteger)
    date = Column(Text)


class Database:
    def __init__(self):
        self.session = Session(bind=engine)

    @staticmethod
    def create_tables():
        Base.metadata.create_all(engine)

    def check_user(self, chat_id):
        return bool(self.session.query(Users).filter_by(chat_id=chat_id).first())

    def add_user(self, chat_id, username):
        self.session.add(Users(chat_id=chat_id, username=username, date=now_date))
        self.session.commit()

    def get_book_list(self):
        self.session.query(Books).all()
