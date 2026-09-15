import aiosqlite
from config import DATABASE_PATH
from utils.helpers import generate_order_id

async def process_instant_purchase(user_id: int, product_id: int) -> dict:
    async with aiosqlite.connect(DATABASE_PATH) as db:
        db.row_factory = aiosqlite.Row
        
        # Check product
        async with db.execute("SELECT * FROM products WHERE id = ?", (product_id,)) as cursor:
            product = await cursor.fetchone()
            if not product:
                return {"success": False, "error": "Product not found"}

        # Check user balance
        async with db.execute("SELECT balance FROM users WHERE user_id = ?", (user_id,)) as cursor:
            user = await cursor.fetchone()
            if not user or user["balance"] < product["price"]:
                return {"success": False, "error": "Insufficient balance"}

        # Check stock key
        async with db.execute(
            "SELECT * FROM product_stock WHERE product_id = ? AND is_sold = 0 LIMIT 1", 
            (product_id,)
        ) as cursor:
            stock_item = await cursor.fetchone()
            if not stock_item:
                return {"success": False, "error": "Out of stock"}

        # Execute transaction atomic
        order_id = generate_order_id()
        
        # Deduct balance
        await db.execute("UPDATE users SET balance = balance - ? WHERE user_id = ?", (product["price"], user_id))
        
        # Mark stock as sold
        await db.execute(
            "UPDATE product_stock SET is_sold = 1, sold_to = ?, sold_at = CURRENT_TIMESTAMP WHERE id = ?",
            (user_id, stock_item["id"])
        )
        
        # Insert order
        await db.execute(
            "INSERT INTO orders (order_id, user_id, product_id, price, status, license_key) VALUES (?, ?, ?, ?, 'COMPLETED', ?)",
            (order_id, user_id, product_id, product["price"], stock_item["license_key"])
        )
        
        await db.commit()
        return {
            "success": True,
            "order_id": order_id,
            "product_name": product["name_bn"],
            "price": product["price"],
            "license_key": stock_item["license_key"]
        }