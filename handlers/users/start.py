from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Command
from utils.db_api.database import DB_Commands
from keyboards.default.location import location
from loader import dp
from states.states import Registration
from filters.isPrivate import IsPrivate
from filters.isGroup import IsGroup
db = DB_Commands()


@dp.message_handler(IsGroup(),CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Siz chatdan foydalanayapsiz")
    user = types.User.get_current()
    k = await db.add_user(user.id,user.username)
    if k:
        await message.answer("Siz ro'yhatdan o'tgansiz, manzil yuboring",reply_markup=location)
        await Registration.manzil.set()
    # await message.answer(f"Yangi kategoriya kiriting:")

# @dp.message_handler(IsGroup(),CommandStart())
# async def bot_start(message: types.Message):
#     await message.answer(f"Groupda foydalanish taqiqlanadi!!")


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def delete_category(message: types.Message):
    if message.text.isdigit():
        a = await db.delete_category(message.text)
        cat = await db.get_categories()
    return ''

@dp.message_handler(content_types=types.ContentTypes.AUDIO)
async def add_category(message: types.Message):
    if not message.text.isdigit():
        a = await db.add_category(message.text)
    cat = await db.get_categories()
    for i in cat:
        print(i.name,i.id)