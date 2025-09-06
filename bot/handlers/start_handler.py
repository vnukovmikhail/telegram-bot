from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def cmd_start(msg: Message, counter: int):
    await msg.answer(f'Hi, res: {counter}.')