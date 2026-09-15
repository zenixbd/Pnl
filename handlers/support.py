from aiogram import Router, F
from aiogram.types import Message
from config import SUPPORT_USERNAME, UPDATES_CHANNEL
from database import get_user_language

router = Router()

@router.message(F.text.in_(["💬 সাপোর্ট", "💬 Support", "ℹ️ তথ্য", "ℹ️ About"]))
async def show_support(message: Message):
    lang = await get_user_language(message.from_user.id)
    
    if lang == "bn":
        text = (
            "<b>💬 কাস্টমার সাপোর্ট ও তথ্য</b>\n\n"
            f"👤 Owner: @{SUPPORT_USERNAME}\n"
            f"📢 Updates: {UPDATES_CHANNEL}\n\n"
            "যে কোনো প্রয়োজনে মেসেজ দিন।"
        )
    else:
        text = (
            "<b>💬 Customer Support & Info</b>\n\n"
            f"👤 Owner: @{SUPPORT_USERNAME}\n"
            f"📢 Updates: {UPDATES_CHANNEL}\n\n"
            "Feel free to reach out for assistance."
        )
    await message.answer(text, parse_mode="HTML")