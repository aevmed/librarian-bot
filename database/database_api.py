from sqlalchemy import create_engine, Column, Integer, Text, BigInteger, Float
from sqlalchemy.orm import declarative_base, Session

engine = create_engine('postgresql://postgres:postgres@localhost:5432/bot')

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(BigInteger)
    username = Column(Text)


class Books(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_name = Column(Text)
    book_author = Column(Text)
    book_description = Column(Text)
    book_owner = Column(BigInteger)
    date = Column(Text)


class Database:
    def __init_(self):
        self.session = Session(bind=engine)

    @staticmethod
    def create_tables():
        Base.metadata.create_all(engine)
