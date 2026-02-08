from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# ====== КНОПКИ ======

BTN_WITHDRAW = "📈 Withdraw"
BTN_SCREEN = "🖼 Generate screenshot"

BTN_SUCCESS = "✅ Successful withdrawal"
BTN_BALANCE = "💼 Balance"
BTN_BACK = "⬅️ Back"

# ====== ГЛАВНОЕ МЕНЮ ======

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=BTN_WITHDRAW)],
        [KeyboardButton(text=BTN_SCREEN)],
    ],
    resize_keyboard=True
)

# ====== МЕНЮ ВИВОДА ======

withdraw_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=BTN_SUCCESS)],
        [KeyboardButton(text=BTN_BALANCE)],
        [KeyboardButton(text=BTN_BACK)],
    ],
    resize_keyboard=True
)
