import random
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent
import asyncio

TOKEN = "8573598759:AAGxl227z696mIZp44Lt3e8JnuIuQzidHhA"

bot = Bot(TOKEN)
dp = Dispatcher()

# --- 1. Личные сообщения ---
@dp.message(F.chat.type == "private")
async def private_reply(message: Message):
    await message.answer("Мне похуй, я мопс")


# --- 2. Группы, супергруппы, каналы ---
@dp.message(F.chat.type.in_(("group", "supergroup", "channel")))
async def group_reply(message: Message):
    # шанс ответа 1 к 200 (можешь изменить)
    if random.randint(1, 10) == 1:
        await message.reply("Мне похуй, я мопс")


# --- 3. Inline Mode ---
@dp.inline_query()
async def inline_mode(query: InlineQuery):
    result = InlineQueryResultArticle(
        id="mops",
        title="Мне похуй, я мопс",
        input_message_content=InputTextMessageContent(
            message_text="Мне похуй, я мопс"
        ),
        description="Отправить фразу"
    )
    await query.answer([result], cache_time=1)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
