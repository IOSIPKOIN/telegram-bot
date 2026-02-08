from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from render import render_html

router = Router()


@router.message(Command("bal"))
async def bal(message: Message):
    path = await render_html("balance.html", "balance.png")
    await message.answer_photo(photo=open(path, "rb"))
