from app.database.database_management import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True
    )

    username = Column(
        String,
        unique=True
    )

    first_name = Column(
        String
    )

    last_name = Column(
        String
    )

    email = Column(
        String,
        unique=True
    )

    password_hash = Column(
        String
    )

class Watchlist(Base):

    __tablename__ = "watchlist"

    id = Column(
        Integer,
        primary_key=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    ticker = Column(
        String
    )
