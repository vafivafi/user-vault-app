from app.db.base import db_settings
from app.schemas.user import UsersSchema
from app.db.models.user import UsersOrm
from secure_python_utils import PasswordService
from app.log.logger import logger
from sqlalchemy import select

class CRUD():
    def __init__(self):
        pass
    
    async def add_user(self, password: str, username: str):
        try:    
            async with db_settings.async_session_factory() as session:
                hesh_password = PasswordService.hash(password)
                new_user = UsersOrm(
                    username = username,
                    password = hesh_password,
                )

                session.add(new_user)
                await session.commit()
                logger.info("Пользователь добавлен")
        except Exception as e:
            logger.error(f"Ошибка при добавлении пользователя {e}")

    async def find_user(self, username: str):
        try:    
            async with db_settings.async_session_factory() as session:
                stmt = select(UsersOrm).where(UsersOrm.username == username)
                result = await session.execute(stmt)
                logger.info("Результат получен")
                return result.scalar_one_or_none()
        except Exception as e:
            logger.error(f"Ошибка при поиске пользователя {e}")


                    

crud = CRUD()