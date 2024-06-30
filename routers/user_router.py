from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from utils import create_preview

router: Router = Router()

@router.message(CommandStart())
async def process_start(message: Message):
    await message.answer("Hi")

@router.message(lambda message: "http" in message.text)
async def process_message(message: Message):
    try:
        url = message.link_preview_options.url
        await message.answer_photo(photo=url)
    except:
        await message.answer(text="Ошибка подключения. Возможно, неверно введена ссылка")
        