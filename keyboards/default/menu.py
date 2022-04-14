#keyboards.default.menu
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="goes"),
        ],
        [
            KeyboardButton(text="go"),
        ],
        [
            KeyboardButton(text="went"),
        ],
        [
            KeyboardButton(text="gone"),
        ],
    ],
    resize_keyboard=True
)

