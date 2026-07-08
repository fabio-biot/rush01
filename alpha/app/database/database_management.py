from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = (
    "postgresql://fabiochaput:Othello06!@localhost:5432/stock_app"
)


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autoflush=False,
    bind=engine
)


Base = declarative_base()