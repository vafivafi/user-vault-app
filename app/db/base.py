from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.core.config import config
from app.db.models.user import Base

class DB_Settings:
    def __init__(self):
        self.async_engine = create_async_engine(config.database_url)

        self.async_session_factory = async_sessionmaker(self.async_engine, expire_on_commit=True)

    @property
    async def create_tables(self):
        async with self.async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    @property
    async def disconnect(self):
        await self.async_engine.dispose()


db_settings = DB_Settings()