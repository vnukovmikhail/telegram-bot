from aiogram import Bot, Dispatcher
from aiogram.methods import DeleteWebhook
from dotenv import load_dotenv
import os, asyncio

from bot.handlers.start_handler import router as start_handler
from bot.middlewares import register_middleware

load_dotenv()

bot = Bot(os.getenv('API_TOKEN'))
dp = Dispatcher()

async def main():
    dp.include_router(start_handler)

    register_middleware(dp)
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass