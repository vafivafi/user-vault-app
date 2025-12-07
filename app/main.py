from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from app.db.base import db_settings
import uvicorn
from app.log.logger import logger
from app.routers import users

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:    
        await db_settings.create_tables
        logger.info("База данных создана")
        
        yield

        await db_settings.disconnect
        logger.info("База данных успешно отключена")

    except Exception as e:
        logger.error(f"Ошибка при запуске {e}")

    

app = FastAPI(lifespan=lifespan)
app.include_router(users.user_router)
