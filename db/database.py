from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase

from core.config import settings


engine  = create_engine(url=settings.DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

class Base(DeclarativeBase):
    pass


def get_db():
    dp = SessionLocal()

    try:
        yield dp
    finally:
        dp.close()



def create_table():
    Base.metadata.create_all(bind=engine)