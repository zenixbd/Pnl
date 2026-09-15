import aiosqlite
from config import DATABASE_PATH

async def create_transaction_record(trx_id: str, user_id: int, amount: float, method: str):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute(
            "INSERT INTO transactions (trx_id, user_id, amount, method, status) VALUES (?, ?, ?, ?, 'PENDING')",
            (trx_id, user_id, amount, method)
        )
        await db.commit()