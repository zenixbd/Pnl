from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def admin_dashboard_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="➕ Add Product", callback_data="admin_add_product"), InlineKeyboardButton(text="📦 Add Stock", callback_data="admin_add_stock")],
        [InlineKeyboardButton(text="💰 Add Balance to User", callback_data="admin_add_user_bal")],
        [InlineKeyboardButton(text="📢 Broadcast Message", callback_data="admin_broadcast")]
    ])