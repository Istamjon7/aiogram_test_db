from aiogram import Dispatcher

from loader import dp
from .isGroup import IsGroup
from .isPrivate import IsPrivate


if __name__ == "filters":
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsPrivate)
