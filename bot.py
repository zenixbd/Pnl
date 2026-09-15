import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from database import init_db

# Import Handlers
from handlers import start, shop, orders, balance, support, admin

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN is missing in .env file!")
        return

    # Init DB
    await init_db()

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Sync Left Side Menu Commands to Telegram
    from services.bot_menu import sync_telegram_side_menu
    await sync_telegram_side_menu(bot)

    # Register Routers
    dp.include_router(start.router)
    dp.include_router(shop.router)
    dp.include_router(orders.router)
    dp.include_router(balance.router)
    dp.include_router(support.router)
    dp.include_router(admin.router)

    logger.info("Bot starting polling...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())