# есть клавиатура reply - снизу поля ввода, а есть inline - под сообщением от бота
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
import app.localization as local

REGISTRATION_SCHEME = [
    [{"text_key": "register", "callback_data": "register"}]
]

GRADES_SCHEME = [
    [{"text_key": "grade7", "callback_data": "grade7"}],
    [{"text_key": "grade8", "callback_data": "grade8"}],
    [{"text_key": "grade9", "callback_data": "grade9"}]
]

MENU_SCHEME = [
    ["my_profile"],
    ["start_task"],
    ["top"]
]

PROFILE_SCHEME = [
    ["change_grade"],
    ["change_lang"],
    ["reminder_switcher"],
    ["technical_support"],
    ["home"]
]

CONFIRMATION_SCHEME = [
    ["yes"],
    ["no"]
]

ANSWER_SCHEME = [
    ["cancel"]
]

BACK_SCHEME = [
    ["home"]
]

TURN_OFF_REMINDER_SCHEME = [
    [{"text_key": "turn_off_reminder", "callback_data": "turn_off_reminder"}]
]

languages = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Latviešu", callback_data="lang_lv")],
    [InlineKeyboardButton(text="English", callback_data="lang_en")],
    [InlineKeyboardButton(text="Русский", callback_data="lang_ru")],
    ])

async def create_reply_keyboard(scheme, lang: str):
    keyboard = [
        [KeyboardButton(text=await local.get_text(lang, text_key)) for text_key in row]
        for row in scheme
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

async def create_inline_keyboard(scheme, lang: str):
    builder = InlineKeyboardBuilder()

    for row in scheme: # проходим по схемам и добавляем кнопки в строки
        for btn in row:
            button_text = await local.get_text(lang, btn["text_key"])
            builder.button(text=button_text, callback_data=btn["callback_data"])

        builder.adjust(1)

    return builder.as_markup()

async def create_multiple_choice_keyboard(choices: list[str]):
    builder = InlineKeyboardBuilder()

    for choice in choices:
        builder.button(text=choice, callback_data=choice)

    builder.adjust(1)  # одна кнопка на строку
    return builder.as_markup()