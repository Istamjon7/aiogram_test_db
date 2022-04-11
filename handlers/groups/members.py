from aiogram.types import ContentType
from aiogram import Bot, types
from filters.isPrivate import IsPrivate
from filters.isGroup import IsGroup
from loader import dp, bot
from datetime import datetime

# ban_users = []
# @dp.message_handler(IsGroup(),content_types=ContentType.NEW_CHAT_MEMBERS)
# async def new_user(message: types.Message):
#     if not message.from_user.id in ban_users:
#         ban_users.append(message.from_user.id)
#     else:
#         await message.chat.kick(message.from_user.id,[datetime.day,datetime.day+3],revoke_messages=True)
#     members = ", ".join([i.get_mention(as_html=True) for i in message.new_chat_members])
#     await message.reply(f"Xush kelibsiz { members }")

# @dp.message_handler(IsGroup(),content_types=ContentType.LEFT_CHAT_MEMBER)
# async def ban_user(message: types.Message):
#     if message.left_chat_member == message.from_user.id:
#         await message.reply(f'{ message.from_user.username } guruhni tark etdi')
#     elif message.from_user.id == (await bot.me).id:
#         return
#     else:
#         await message.reply(f'{ message.from_user.username } tark edi')