import logging
from config import BINANCE_PAY_ID, USDT_BDT_RATE

logger = logging.getLogger(__name__)

class BinancePayService:
    @staticmethod
    def get_binance_info():
        return {
            "pay_id": BINANCE_PAY_ID,
            "rate": USDT_BDT_RATE
        }

    @staticmethod
    async def verify_transaction(trx_id: str) -> bool:
        # Placeholder for real Binance merchant API verification
        return len(trx_id) >= 6