from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from database import fetch_products, get_available_stock_count, get_user_language
from utils.i18n import get_text
from services.delivery import process_instant_purchase

router = Router()

@router.message(F.text.in_(["🎮 প্যানেল শপ", "🎮 Panel Shop", "📦 প্রোডাক্টস", "📦 Products"]))
async def show_shop_products(message: Message):
    lang = await get_user_language(message.from_user.id)
    products = await fetch_products()
    
    if not products:
        await message.answer("❌ No products available right now.")
        return

    for prod in products:
        stock = await get_available_stock_count(prod["id"])
        name = prod["name_bn"] if lang == "bn" else prod["name_en"]
        desc = prod["description_bn"] if lang == "bn" else prod["description_en"]
        
        card_text = (
            f"<b>🎮 {name}</b>\n\n"
            f"📝 {desc}\n\n"
            f"💰 Price: ৳{prod['price']:.2f} BDT\n"
            f"📦 Stock: <b>{stock}</b> available\n"
            f"⏳ Validity: {prod['duration_days']} Days"
        )
        
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🛒 Buy Now", callback_data=f"buy_prod_{prod['id']}")]
        ])
        await message.answer(card_text, parse_mode="HTML", reply_markup=kb)

@router.callback_query(F.data.startswith("buy_prod_"))
async def handle_buy_product(callback: CallbackQuery):
    product_id = int(callback.data.split("_")[-1])
    user_id = callback.from_user.id
    lang = await get_user_language(user_id)
    
    result = await process_instant_purchase(user_id, product_id)
    
    if not result["success"]:
        err_msg = get_text("out_of_stock" if result["error"] == "Out of stock" else "insufficient_balance", lang)
        await callback.answer(err_msg, show_alert=True)
        return

    success_msg = get_text(
        "order_success", lang,
        order_id=result["order_id"],
        product=result["product_name"],
        price=result["price"],
        key=result["license_key"]
    )
    await callback.message.answer(success_msg, parse_mode="HTML")
    await callback.answer()