from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from models import error_history, known_error, user
from models.base import Base

DATABASE_URL = "sqlite+aiosqlite:///./database.db"

engine = create_async_engine(DATABASE_URL, echo=True)

async_session_maker = async_sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)


async def get_async_session():
    async with async_session_maker() as session:
        yield session


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
