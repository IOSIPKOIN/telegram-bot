import asyncio
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from handlers.balance import router as balance_router
from handlers.success import router as success_router
from handlers.screenshot import router as screenshot_router   # ← ДОБАВЬ ЭТО


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(balance_router)
    dp.include_router(success_router)
    dp.include_router(screenshot_router)   # ← И ЭТО

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
