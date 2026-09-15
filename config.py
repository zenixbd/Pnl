import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("8850971652:AAH7_6z53xRZT77D714JxeoDbuNC_TDqLyc", "")
ADMIN_ID = int(os.getenv("7110008559", "0"))
SUPPORT_USERNAME = os.getenv("TEAM_X_BD1M", "Support")
UPDATES_CHANNEL = os.getenv("TEAM_X_BD", "")
DATABASE_PATH = os.getenv("DATABASE_PATH", "freefire_shop.db")

BKASH_NUMBER = os.getenv("BKASH_NUMBER", "01767309655")
NAGAD_NUMBER = os.getenv("NAGAD_NUMBER", "01322250788")
ROCKET_NUMBER = os.getenv("ROCKET_NUMBER", "01767309655")
MIN_RECHARGE = float(os.getenv("MIN_RECHARGE", "10"))

BINANCE_PAY_ID = os.getenv("BINANCE_PAY_ID", "1262150030")
BINANCE_API_KEY = os.getenv("XrETeJpknpL8L0lZUESfkc8TWJYeFE7UiOvqrQYgssrwG3ifwULE6ib7snibaXkF", "")
BINANCE_SECRET_KEY = os.getenv("Dt2V1RoGplA9xJ1WwVpx0gbsUfOCA8AVWQ038f8jObWiK29wiFzCVslv5GNyzmb2", "")
BINANCE_MERCHANT_ID = os.getenv("BINANCE_MERCHANT_ID", "")
USDT_BDT_RATE = float(os.getenv("USDT_BDT_RATE", "120"))