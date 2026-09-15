from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from utils.security import is_admin
from keyboards.admin import admin_dashboard_keyboard

router = Router()

@router.message(Command("admin"))
async def cmd_admin(message: Message):
    if not is_admin(message.from_user.id):
        return
    
    await message.answer("<b>⚡ JIHAD BHAI Admin Dashboard</b>", parse_mode="HTML", reply_markup=admin_dashboard_keyboard())