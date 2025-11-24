from application.core.configuration import settings
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine(settings.CREATE_ASYNC_ENGINE())
session = async_sessionmaker(engine)


class Base(DeclarativeBase):
    pass
