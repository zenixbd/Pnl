import random
import string

def generate_order_id() -> str:
    digits = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"JH-{digits}"

def generate_trx_id() -> str:
    digits = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return f"TRX-{digits}"