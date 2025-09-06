from aiogram import Dispatcher

from bot.middlewares.init_middleware import InitMiddleware

def register_middleware(dp: Dispatcher):
    dp.update.middleware(InitMiddleware())