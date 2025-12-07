from fastapi import APIRouter, HTTPException
from app.db.CRUD.user_repository import crud
from app.schemas.user import UsersSchema, FindUsersSchema
from app.log.logger import logger

user_router = APIRouter(prefix="/users", tags=['users'])

@user_router.post("/add-user", summary="Добавить пользователя")
async def add_user(cred: UsersSchema):
    await crud.add_user(cred.password, cred.username)
    logger.info("Функция выполнила работу успешно")

    return {"status" : True, "message" : "Пользователь добавлен"}

@user_router.post("/get-user", summary="Найти пользователя по username")
async def get_user(find_user: FindUsersSchema):
    user = await crud.find_user(find_user.username)
    if not user:
        logger.error(f"Пользователь {find_user.username} не найден")
        raise HTTPException(status_code=404, detail=f"Пользователь {find_user.username} не найден")
    
    logger.info(f"Пользователь {user} найден")
    return {"message": "пользователь найден", "пользователь" : user.username}
    