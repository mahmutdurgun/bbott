import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")
TESTNET = os.getenv("BINANCE_TESTNET") == "true"

SYMBOL = os.getenv("SYMBOL", "BTCUSDT")
TRADE_QTY = float(os.getenv("TRADE_QTY", 0.001))
