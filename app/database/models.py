import datetime

from sqlalchemy import Column, Integer, DATE, String

from app.database.db_connect import Base


class User(Base):
    __tablename__ = "users"

    # Telegram user id
    user_id = Column(Integer, primary_key=True, unique=True, nullable=False)

    # Telegram user username
    username = Column(String(32), nullable=False)

    # User email
    email = Column(String, nullable=False, unique=True)

    # User mobile phone
    mb_phone = Column(String, nullable=False, unique=True)

    # User Password
    password = Column(String, nullable=False)

    # registration date
    reg_date = Column(DATE, default=datetime.date.today())

    # update date
    update_date = Column(DATE, default=datetime.date.today())

    def __str__(self) -> str:
        return f"<User:{self.user_id}>"
