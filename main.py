from aiogram import Bot, Dispatcher
from aiogram.methods import DeleteWebhook
from dotenv import load_dotenv
import os, asyncio

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from bot.db.models import BaseModel 
from bot.handlers.start_handler import router as start_handler
from bot.middlewares import register_middleware

load_dotenv()

bot = Bot(os.getenv('API_TOKEN'))
dp = Dispatcher()

async def init_model(engine):
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)

async def main():
    dp.include_router(start_handler)

    engine = create_async_engine(url="sqlite+aiosqlite:///data.db")
    session_maker = async_sessionmaker(engine, expire_on_commit=False)

    register_middleware(dp, session_maker)
    await init_model(engine)
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass