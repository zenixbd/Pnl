from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from database import get_user, get_user_language
from keyboards.user import payment_methods_keyboard
from utils.i18n import get_text
from config import BKASH_NUMBER, NAGAD_NUMBER, ROCKET_NUMBER, MIN_RECHARGE, BINANCE_PAY_ID, USDT_BDT_RATE

router = Router()

@router.message(F.text.in_(["💰 ব্যালেন্স", "💰 Balance"]))
async def show_balance_info(message: Message):
    user_id = message.from_user.id
    lang = await get_user_language(user_id)
    user = await get_user(user_id)
    
    bal = user["balance"] if user else 0.0
    text = get_text("balance_info", lang, balance=bal)
    await message.answer(text, parse_mode="HTML", reply_markup=payment_methods_keyboard(lang))

@router.callback_query(F.data.startswith("pay_"))
async def handle_payment_method(callback: CallbackQuery):
    method = callback.data.split("_")[-1]
    lang = await get_user_language(callback.from_user.id)
    
    if method == "bkash":
        msg = get_text("mfs_instruction", lang, method="bKash", number=BKASH_NUMBER, min_deposit=MIN_RECHARGE)
    elif method == "nagad":
        msg = get_text("mfs_instruction", lang, method="Nagad", number=NAGAD_NUMBER, min_deposit=MIN_RECHARGE)
    elif method == "rocket":
        msg = get_text("mfs_instruction", lang, method="Rocket", number=ROCKET_NUMBER, min_deposit=MIN_RECHARGE)
    elif method == "binance":
        msg = get_text("binance_instruction", lang, pay_id=BINANCE_PAY_ID, rate=USDT_BDT_RATE)
    else:
        msg = "Invalid Method"

    await callback.message.answer(msg, parse_mode="HTML")
    await callback.answer()