# Multilingual (Bangla & English) Dictionary

TEXTS = {
    "welcome": {
        "bn": "<b>🔥 JIHAD BHAI FREE FIRE PANEL SHOP 🔥</b>\n\nস্বাগতম, <b>{name}</b>!\nID: <code>{user_id}</code>\n\nআমাদের অটোমেটিক শপ থেকে খুব সহজেই প্রিমিয়াম ফ্রি ফায়ার প্যানেল ও লাইসেন্স কি কিনতে পারবেন।",
        "en": "<b>🔥 JIHAD BHAI FREE FIRE PANEL SHOP 🔥</b>\n\nWelcome, <b>{name}</b>!\nID: <code>{user_id}</code>\n\nEasily purchase premium Free Fire panels & license keys instantly from our automated store."
    },
    "menu_shop": {"bn": "🎮 প্যানেল শপ", "en": "🎮 Panel Shop"},
    "menu_orders": {"bn": "🛒 আমার অর্ডার", "en": "🛒 My Orders"},
    "menu_balance": {"bn": "💰 ব্যালেন্স", "en": "💰 Balance"},
    "menu_products": {"bn": "📦 প্রোডাক্টস", "en": "📦 Products"},
    "menu_support": {"bn": "💬 সাপোর্ট", "en": "💬 Support"},
    "menu_language": {"bn": "🌐 ভাষা / Language", "en": "🌐 Language / ভাষা"},
    "menu_about": {"bn": "ℹ️ তথ্য", "en": "ℹ️ About"},

    "select_language": {
        "bn": "আপনার পছন্দের ভাষা নির্বাচন করুন:",
        "en": "Select your preferred language:"
    },
    "lang_changed": {
        "bn": "✅ ভাষা পরিবর্তন সফল হয়েছে!",
        "en": "✅ Language changed successfully!"
    },

    "balance_info": {
        "bn": "💰 <b>আপনার একাউন্ট ব্যালেন্স:</b> ৳{balance:.2f} BDT\n\nব্যালেন্স রিচার্জ করতে নিচের বাটনে চাপ দিন।",
        "en": "💰 <b>Your Account Balance:</b> ৳{balance:.2f} BDT\n\nClick the button below to add funds."
    },
    "add_balance_btn": {"bn": "💳 ব্যালেন্স যোগ করুন", "en": "💳 Add Balance"},

    "payment_methods": {
        "bn": "<b>💳 পেমেন্ট মাধ্যম নির্বাচন করুন:</b>\n\nযে উপায়ে আপনি ব্যালেন্স ডিপোজিট করতে চান:",
        "en": "<b>💳 Select Payment Method:</b>\n\nChoose your preferred deposit method:"
    },

    "mfs_instruction": {
        "bn": "<b>💳 {method} পেমেন্ট নির্দেশনা:</b>\n\nআমাদের {method} নম্বর: <code>{number}</code> (Personal)\n\n১. টাকা Send Money করুন।\n২. মিনিমাম ডিপোজিট: ৳{min_deposit} BDT\n৩. টাকা পাঠানোর পর TrxID লিখুন।",
        "en": "<b>💳 {method} Payment Instructions:</b>\n\nOur {method} Number: <code>{number}</code> (Personal)\n\n1. Send Money to this number.\n2. Minimum Deposit: ৳{min_deposit} BDT\n3. Submit your Transaction ID (TrxID) after payment."
    },

    "binance_instruction": {
        "bn": "<b>🔶 Binance Pay (USDT) নির্দেশনা:</b>\n\nBinance Pay ID: <code>{pay_id}</code>\nবর্তমান রেট: $1 USDT = ৳{rate} BDT\n\n১. Binance অ্যাপ খুলুন এবং Pay ID-তে USDT পাঠান।\n২. পেমেন্ট সম্পন্ন হলে Transaction / Order ID বা স্ক্রিনশট সাবমিট করুন।",
        "en": "<b>🔶 Binance Pay (USDT) Instructions:</b>\n\nBinance Pay ID: <code>{pay_id}</code>\nCurrent Exchange Rate: $1 USDT = ৳{rate} BDT\n\n1. Open Binance app and transfer USDT to the Pay ID.\n2. Submit the Transaction / Order ID once completed."
    },

    "out_of_stock": {
        "bn": "❌ দুঃখিত, এই মুহূর্তে প্রোডাক্টটি স্টকে নেই!",
        "en": "❌ Sorry, this item is currently out of stock!"
    },
    "insufficient_balance": {
        "bn": "❌ পর্যাপ্ত ব্যালেন্স নেই! আপনার ব্যালেন্স: ৳{balance:.2f} BDT",
        "en": "❌ Insufficient balance! Your balance: ৳{balance:.2f} BDT"
    },
    "order_success": {
        "bn": "✅ <b>পেমেন্ট সফল ও প্রোডাক্ট ডেলিভারি!</b>\n\n🧾 অর্ডার আইডি: <code>#{order_id}</code>\n🎮 প্রোডাক্ট: {product}\n💰 মাইনাস ব্যালেন্স: ৳{price:.2f}\n\n🔑 <b>আপনার লাইসেন্স কী:</b>\n<code>{key}</code>",
        "en": "✅ <b>Payment Successful & Product Delivered!</b>\n\n🧾 Order ID: <code>#{order_id}</code>\n🎮 Product: {product}\n💰 Deducted: ৳{price:.2f}\n\n🔑 <b>Your License Key:</b>\n<code>{key}</code>"
    }
}

def get_text(key: str, lang: str = "bn", **kwargs) -> str:
    lang_dict = TEXTS.get(key, {})
    template = lang_dict.get(lang, lang_dict.get("bn", ""))
    return template.format(**kwargs) if kwargs else template