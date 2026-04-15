from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Task categories
CATEGORIES = [
    "\u0423\u0431\u043e\u0440\u043a\u0430",
    "\u041f\u043e\u043a\u0443\u043f\u043a\u0438",
    "\u0420\u0430\u0441\u0442\u0435\u043d\u0438\u044f",
    "\u0413\u043e\u0442\u043e\u0432\u043a\u0430",
    "\u041f\u0438\u0442\u043e\u043c\u0446\u044b",
    "\u0414\u0440\u0443\u0433\u043e\u0435",
]


def get_main_menu() -> ReplyKeyboardMarkup:
    """Main bot menu."""
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="\u2795 \u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443")],
            [KeyboardButton(text="\U0001F4CB \u041c\u043e\u0438 \u0437\u0430\u0434\u0430\u0447\u0438")],
            [KeyboardButton(text="\u2705 \u041e\u0442\u043c\u0435\u0442\u0438\u0442\u044c \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439")],
            [KeyboardButton(text="\U0001F5D1 \u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443")],
        ],
        resize_keyboard=True,
    )


def get_categories_keyboard() -> ReplyKeyboardMarkup:
    """Keyboard with task categories."""
    rows = [[KeyboardButton(text=category)] for category in CATEGORIES]
    rows.append([KeyboardButton(text="/cancel")])
    return ReplyKeyboardMarkup(keyboard=rows, resize_keyboard=True)
