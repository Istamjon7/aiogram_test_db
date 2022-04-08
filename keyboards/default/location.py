from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

location = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Lokatsiya',request_location=True)
        ]
    ],
    resize_keyboard=True
)