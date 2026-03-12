from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from core.config import settings


engine  = create_engine(url=settings.DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()


def get_db():
    dp = SessionLocal()

    try:
        yield dp
    finally:
        dp.close()



def create_table():
    Base.metadata.create_all(bind=engine)