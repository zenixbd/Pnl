from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from database import create_or_update_user, get_user_language, set_user_language
from keyboards.user import main_keyboard, language_keyboard
from utils.i18n import get_text

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    user = message.from_user
    await create_or_update_user(user.id, user.username, user.full_name)
    lang = await get_user_language(user.id)
    
    welcome_msg = get_text("welcome", lang, name=user.full_name, user_id=user.id)
    await message.answer(welcome_msg, parse_mode="HTML", reply_markup=main_keyboard(lang))

@router.message(F.text.in_(["🌐 भाषा / Language", "Language"]))
async def show_language_options(message: Message):
    lang = await get_user_language(message.from_user.id)
    await message.answer(get_text("select_language", lang), reply_markup=language_keyboard())

@router.callback_query(F.data.startswith("set_lang_"))
async def process_language_change(callback: CallbackQuery):
    new_lang = callback.data.split("_")[-1]
    await set_user_language(callback.from_user.id, new_lang)
    
    await callback.answer(get_text("lang_changed", new_lang))
    await callback.message.answer(
        get_text("welcome", new_lang, name=callback.from_user.full_name, user_id=callback.from_user.id),
        parse_mode="HTML",
        reply_markup=main_keyboard(new_lang)
    )