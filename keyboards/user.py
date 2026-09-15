from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from utils.i18n import get_text

def main_keyboard(lang: str = "bn") -> ReplyKeyboardMarkup:
    kb = [
        [KeyboardButton(text=get_text("menu_shop", lang)), KeyboardButton(text=get_text("menu_orders", lang))],
        [KeyboardButton(text=get_text("menu_balance", lang)), KeyboardButton(text=get_text("menu_products", lang))],
        [KeyboardButton(text=get_text("menu_support", lang)), KeyboardButton(text=get_text("menu_language", lang))],
        [KeyboardButton(text=get_text("menu_about", lang))]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def language_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🇧🇩 বাংলা (Bangla)", callback_data="set_lang_bn"),
            InlineKeyboardButton(text="🇺🇸 English", callback_data="set_lang_en")
        ]
    ])

def payment_methods_keyboard(lang: str = "bn") -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="💳 bKash", callback_data="pay_bkash"),
            InlineKeyboardButton(text="💳 Nagad", callback_data="pay_nagad")
        ],
        [
            InlineKeyboardButton(text="💳 Rocket", callback_data="pay_rocket"),
            InlineKeyboardButton(text="🔶 Binance Pay (USDT)", callback_data="pay_binance")
        ]
    ])