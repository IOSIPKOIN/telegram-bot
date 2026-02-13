from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from render import render_html

router = Router()


@router.message(Command("bal"))
async def bal(message: Message):
    try:
        _, data = message.text.split("/bal", 1)
        user, balance, failed, success = [x.strip() for x in data.split(",")]
    except:
        await message.answer(
            "Формат:\n/bal Имя, Баланс, Failed, Success\n\n"
            "Пример:\n/bal Alex, 12500, 5400, 2000"
        )
        return

    path = await render_html(
        "balance.html",
        "balance.png",
        user=user,
        balance=balance,
        failed=failed,
        success=success
    )

    await message.answer_photo(photo=open(path, "rb"))
