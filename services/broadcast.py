import aiosqlite
import logging
from config import DATABASE_PATH

logger = logging.getLogger(__name__)

async def get_all_user_ids():
    async with aiosqlite.connect(DATABASE_PATH) as db:
        async with db.execute("SELECT user_id FROM users") as cursor:
            rows = await cursor.fetchall()
            return [row[0] for row in rows]