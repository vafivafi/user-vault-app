from fastapi import APIRouter
from app.db.CRUD.user_repository import crud
from app.schemas.user import UsersSchema
from app.log.logger import logger

reg_router = APIRouter(prefix="/users", tags=['users'])

@reg_router.post("/add-user")
async def add_ser(cred: UsersSchema):
    await crud.add_user(cred.password, cred.username)
    logger.info("Функция выполнила работу успешно")

    return {"status" : True, "message" : "Пользователь добавлен"}