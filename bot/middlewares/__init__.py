from aiogram import Dispatcher

from bot.middlewares.init_middleware import InitMiddleware

def register_middleware(dp: Dispatcher, session_maker):
    dp.update.middleware(InitMiddleware(session_maker))