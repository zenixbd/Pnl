import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))
SUPPORT_USERNAME = os.getenv("SUPPORT_USERNAME", "Support")
UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "")
DATABASE_PATH = os.getenv("DATABASE_PATH", "freefire_shop.db")

BKASH_NUMBER = os.getenv("BKASH_NUMBER", "01700000000")
NAGAD_NUMBER = os.getenv("NAGAD_NUMBER", "01800000000")
ROCKET_NUMBER = os.getenv("ROCKET_NUMBER", "01900000000")
MIN_RECHARGE = float(os.getenv("MIN_RECHARGE", "50"))

BINANCE_PAY_ID = os.getenv("BINANCE_PAY_ID", "123456789")
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY", "")
BINANCE_SECRET_KEY = os.getenv("BINANCE_SECRET_KEY", "")
BINANCE_MERCHANT_ID = os.getenv("BINANCE_MERCHANT_ID", "")
USDT_BDT_RATE = float(os.getenv("USDT_BDT_RATE", "120"))
