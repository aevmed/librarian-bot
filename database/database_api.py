import datetime

from sqlalchemy import create_engine, Column, Integer, Text, BigInteger, Float
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.sql.expression import or_

now_date = datetime.datetime.now()
now_date = now_date.strftime('%Y-%m-%d %H:%M:%S')

# Создаем соединение
engine = create_engine('postgresql://postgres:postgres@localhost:5432/bot')

Base = declarative_base()


# Таблица users
class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(BigInteger)
    username = Column(Text)
    date = Column(Text)


# Таблица books
class Books(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_name = Column(Text)
    book_author = Column(Text)
    book_description = Column(Text)
    book_genre = Column(Text)
    book_owner = Column(BigInteger)
    date = Column(Text)


# database api
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
        return self.session.query(Books).all()

    def get_found_books_by_key_word(self, key_word):
        return self.session.query(Books).filter(
                or_(
                    Books.book_name.like(f'%{key_word}%'),
                    Books.book_author.like(f'%{key_word}%'),
                    Books.book_genre.like(f'%{key_word}%')
                   )
                ).all()

    def get_book(self, book_id):
        return self.session.query(Books).filter_by(id=book_id).first()

    def add_book(self, book_name, book_author, book_description, book_genre, chat_id):
        self.session.add(Books(book_name=book_name, book_author=book_author, book_description=book_description,
                               book_genre=book_genre, book_owner=chat_id, date=now_date))
        self.session.commit()

    def get_my_book_list(self, chat_id):
        return self.session.query(Books).filter_by(book_owner=chat_id).all()

    def delete_book(self, book_id):
        self.session.query(Books).filter_by(id=book_id).delete()
        self.session.commit()
