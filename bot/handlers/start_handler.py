from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.db.repositories.user_repo import UserRepo

router = Router()

@router.message(CommandStart())
async def cmd_start(msg: Message, user_repo: UserRepo):
    await user_repo.create_or_update_user(
        tg_id=msg.from_user.id,
        full_name=msg.from_user.full_name,
        user_name=msg.from_user.username,
    )
    await msg.answer(f'Hi!')