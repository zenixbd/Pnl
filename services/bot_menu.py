import logging
from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault
from database import get_bot_commands

logger = logging.getLogger(__name__)

async def sync_telegram_side_menu(bot: Bot):
    try:
        commands_data = await get_bot_commands()
        
        # Set Default / English Menu
        commands_en = [
            BotCommand(command=row["command"], description=row["desc_en"])
            for row in commands_data
        ]
        await bot.set_my_commands(commands=commands_en, scope=BotCommandScopeDefault())
        
        # Set Bangla Menu for Bangla language code
        commands_bn = [
            BotCommand(command=row["command"], description=row["desc_bn"])
            for row in commands_data
        ]
        await bot.set_my_commands(commands=commands_bn, scope=BotCommandScopeDefault(), language_code="bn")
        
        logger.info("Bot side menu commands synced successfully with Telegram!")
        return True
    except Exception as e:
        logger.error(f"Failed to sync bot side menu: {e}")
        return False