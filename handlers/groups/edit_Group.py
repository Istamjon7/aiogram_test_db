import io
from aiogram.types import ContentType
from data.config import ADMINS
from aiogram import Bot, types
from aiogram.dispatcher.filters.builtin import CommandStart, Command
from filters.isGroup import IsGroup
from loader import dp, bot

@dp.message_handler(IsGroup(),commands=['set'])
async def set_title(message:types.Message):
    source_message = message.reply_to_message
    title = message.new_chat_title(source_message)
    print(title)
    await bot.set_chat_title(message.chat.id, title=title)