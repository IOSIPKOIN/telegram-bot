from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from render import render_html

router = Router()


@router.message(Command("suc"))
async def suc(message: Message):
    path = await render_html("success.html", "success.png")
    await message.answer_photo(photo=open(path, "rb"))
