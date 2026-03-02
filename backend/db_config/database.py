from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

import os

# Updated to use PostgreSQL with the asyncpg driver
DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql+asyncpg://hrms_db_crvl_user:dfRV54mYDp6BfP0vNzO50b59VsEMSK6n@dpg-d6iq2at6ubrc73cets4g-a.oregon-postgres.render.com/hrms_db_crvl"
)

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

Base = declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
