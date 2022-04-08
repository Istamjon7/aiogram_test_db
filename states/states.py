from aiogram.dispatcher.filters.state import State, StatesGroup

class Registration(StatesGroup):
    manzil = State()
    confirm = State()