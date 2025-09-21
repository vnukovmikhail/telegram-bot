from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

MAIN = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='📝 Dialog', callback_data='d')],
])