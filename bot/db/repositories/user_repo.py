from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from bot.db.models.user_model import UserModel

class UserRepo:
    def __init__(self, session: AsyncSession):
        self.__session = session
   
    async def get_user_by_tg_id(self, tg_id: int) -> UserModel:
        statement = select(UserModel).where(UserModel.tg_id == tg_id)
        return await self.__session.scalar(statement)

    async def create_or_update_user(self,
        tg_id: int, full_name: str, user_name: str
    ) -> UserModel:
        user = await self.get_user_by_tg_id(tg_id)

        if not user:
            await self.create_user(tg_id, full_name, user_name)
        else:
            user.user_name = user_name
            user.full_name = full_name

        await self.__session.commit()

    async def create_user(self,
        tg_id: int, full_name: str, user_name: str
    ) -> UserModel:
        user = UserModel(
            tg_id=tg_id,
            full_name=full_name,
            user_name=user_name,
        )
        self.__session.add(user)