from aiogram import Router, F
from aiogram.types import Message
import aiosqlite
from config import DATABASE_PATH
from database import get_user_language

router = Router()

@router.message(F.text.in_(["🛒 আমার অর্ডার", "🛒 My Orders"]))
async def show_user_orders(message: Message):
    user_id = message.from_user.id
    lang = await get_user_language(user_id)
    
    async with aiosqlite.connect(DATABASE_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            "SELECT o.*, p.name_bn, p.name_en FROM orders o JOIN products p ON o.product_id = p.id WHERE o.user_id = ? ORDER BY o.created_at DESC LIMIT 5",
            (user_id,)
        ) as cursor:
            orders = await cursor.fetchall()
            
    if not orders:
        txt = "আপনার কোনো পূববর্তী অর্ডার নেই।" if lang == "bn" else "You have no previous orders."
        await message.answer(txt)
        return

    msg = "<b>📜 আপনার সাম্প্রতিক অর্ডারসমূহ:</b>\n\n" if lang == "bn" else "<b>📜 Your Recent Orders:</b>\n\n"
    for o in orders:
        p_name = o["name_bn"] if lang == "bn" else o["name_en"]
        msg += f"🧾 Order: <code>#{o['order_id']}</code>\n🎮 {p_name}\n💰 ৳{o['price']:.2f}\n🔑 Key: <code>{o['license_key']}</code>\n\n"
        
    await message.answer(msg, parse_mode="HTML")