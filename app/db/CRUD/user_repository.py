from app.db.base import db_settings
from app.schemas.user import UsersSchema
from app.db.models.user import UsersOrm
from secure_python_utils import PasswordService
from app.log.logger import logger

class CRUD():
    def __init__(self):
        pass
    
    async def add_user(self, password: str, username: str):
        async with db_settings.async_session_factory() as session:
            hesh_password = PasswordService.hash(password)
            new_user = UsersOrm(
                username = username,
                password = hesh_password,
            )

            session.add(new_user)
            await session.commit()
            logger.info("Пользователь добавлен")
        
crud = CRUD()