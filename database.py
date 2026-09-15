import aiosqlite
import logging
from config import DATABASE_PATH

logger = logging.getLogger(__name__)

async def init_db():
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute("PRAGMA foreign_keys = ON;")
        
        # Users Table
        await db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            full_name TEXT,
            balance REAL DEFAULT 0.0,
            language TEXT DEFAULT 'bn',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)
        
        # Products Table
        await db.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name_bn TEXT NOT NULL,
            name_en TEXT NOT NULL,
            description_bn TEXT,
            description_en TEXT,
            price REAL NOT NULL,
            duration_days INTEGER DEFAULT 30,
            is_active INTEGER DEFAULT 1,
            image_url TEXT
        );
        """)
        
        # Inventory / Stock Table
        await db.execute("""
        CREATE TABLE IF NOT EXISTS product_stock (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            license_key TEXT NOT NULL,
            is_sold INTEGER DEFAULT 0,
            sold_to INTEGER,
            sold_at TIMESTAMP,
            FOREIGN KEY (product_id) REFERENCES products (id) ON DELETE CASCADE
        );
        """)
        
        # Orders Table
        await db.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id TEXT PRIMARY KEY,
            user_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            price REAL NOT NULL,
            status TEXT DEFAULT 'PENDING',
            license_key TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (user_id),
            FOREIGN KEY (product_id) REFERENCES products (id)
        );
        """)
        
        # Transactions Table
        await db.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            trx_id TEXT PRIMARY KEY,
            user_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            method TEXT NOT NULL,
            status TEXT DEFAULT 'PENDING',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (user_id)
        );
        """)

        # Bot Dynamic Settings Table (For Reply Keyboards)
        await db.execute("""
        CREATE TABLE IF NOT EXISTS bot_settings (
            key_name TEXT PRIMARY KEY,
            val_bn TEXT NOT NULL,
            val_en TEXT NOT NULL
        );
        """)

        # Insert default reply keyboard labels if not exists
        default_settings = [
            ('btn_shop', '🛒 প্যানেল শপ (Shop)', '🛒 Panel Shop'),
            ('btn_recharge', '💳 ব্যালেন্স রিচার্জ', '💳 Recharge Balance'),
            ('btn_orders', '📦 আমার অর্ডারসমূহ', '📦 My Orders'),
            ('btn_profile', '👤 আমার প্রোফাইল', '👤 My Profile'),
            ('btn_support', '💬 কাস্টমার সাপোর্ট', '💬 Support'),
            ('btn_lang', '🌐 ভাষা / Language', '🌐 Language')
        ]
        for key, val_bn, val_en in default_settings:
            await db.execute("""
            INSERT OR IGNORE INTO bot_settings (key_name, val_bn, val_en)
            VALUES (?, ?, ?)
            """, (key, val_bn, val_en))

        # Bot Commands Table (For Left Side Menu)
        await db.execute("""
        CREATE TABLE IF NOT EXISTS bot_commands (
            command TEXT PRIMARY KEY,
            desc_bn TEXT NOT NULL,
            desc_en TEXT NOT NULL
        );
        """)

        default_commands = [
            ('start', 'বট পুনরায় শুরু করুন / Main Menu', 'Restart Bot / Main Menu'),
            ('shop', 'ফ্রি ফায়ার প্যানেল কিনুন', 'Buy Free Fire Panels'),
            ('recharge', 'টাকা যোগ করুন (bKash/Nagad/Binance)', 'Add Balance'),
            ('orders', 'আপনার কেনা কি (Key) দেখুন', 'View Purchased Keys'),
            ('support', 'সাহায্য এবং কাস্টমার কেয়ার', 'Customer Support / Helpline'),
            ('lang', 'ভাষা পরিবর্তন করুন', 'Change Language')
        ]
        for cmd, d_bn, d_en in default_commands:
            await db.execute("""
            INSERT OR IGNORE INTO bot_commands (command, desc_bn, desc_en)
            VALUES (?, ?, ?)
            """, (cmd, d_bn, d_en))

        await db.commit()
        logger.info("Database initialized successfully with dynamic setting tables.")

async def get_user(user_id: int):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)) as cursor:
            return await cursor.fetchone()

async def create_or_update_user(user_id: int, username: str, full_name: str):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute("""
        INSERT INTO users (user_id, username, full_name, language)
        VALUES (?, ?, ?, 'bn')
        ON CONFLICT(user_id) DO UPDATE SET
            username = excluded.username,
            full_name = excluded.full_name;
        """, (user_id, username or "", full_name or ""))
        await db.commit()

async def set_user_language(user_id: int, lang: str):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute("UPDATE users SET language = ? WHERE user_id = ?", (lang, user_id))
        await db.commit()

async def get_user_language(user_id: int) -> str:
    user = await get_user(user_id)
    return user["language"] if user and user["language"] else "bn"

async def update_balance(user_id: int, amount: float):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute("UPDATE users SET balance = balance + ? WHERE user_id = ?", (amount, user_id))
        await db.commit()

async def get_available_stock_count(product_id: int) -> int:
    async with aiosqlite.connect(DATABASE_PATH) as db:
        async with db.execute(
            "SELECT COUNT(*) FROM product_stock WHERE product_id = ? AND is_sold = 0",
            (product_id,)
        ) as cursor:
            res = await cursor.fetchone()
            return res[0] if res else 0

async def fetch_products():
    async with aiosqlite.connect(DATABASE_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("SELECT * FROM products WHERE is_active = 1") as cursor:
            return await cursor.fetchall()

async def fetch_product_by_id(product_id: int):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("SELECT * FROM products WHERE id = ?", (product_id,)) as cursor:
            return await cursor.fetchone()

async def get_bot_settings():
    async with aiosqlite.connect(DATABASE_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("SELECT * FROM bot_settings") as cursor:
            rows = await cursor.fetchall()
            res = {}
            for row in rows:
                res[row["key_name"]] = {"bn": row["val_bn"], "en": row["val_en"]}
            return res

async def update_bot_setting(key_name: str, val_bn: str, val_en: str):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute("""
        INSERT INTO bot_settings (key_name, val_bn, val_en)
        VALUES (?, ?, ?)
        ON CONFLICT(key_name) DO UPDATE SET
            val_bn = excluded.val_bn,
            val_en = excluded.val_en;
        """, (key_name, val_bn, val_en))
        await db.commit()

async def get_bot_commands():
    async with aiosqlite.connect(DATABASE_PATH) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute("SELECT * FROM bot_commands") as cursor:
            return await cursor.fetchall()

async def update_bot_command(command: str, desc_bn: str, desc_en: str):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute("""
        INSERT INTO bot_commands (command, desc_bn, desc_en)
        VALUES (?, ?, ?)
        ON CONFLICT(command) DO UPDATE SET
            desc_bn = excluded.desc_bn,
            desc_en = excluded.desc_en;
        """, (command, desc_bn, desc_en))
        await db.commit()