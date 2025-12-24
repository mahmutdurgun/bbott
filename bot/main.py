from binance.client import Client
from config import API_KEY, API_SECRET, TESTNET, SYMBOL, TRADE_QTY
from strategy import simple_decision
import time

def main():
    client = Client(API_KEY, API_SECRET)

    if TESTNET:
        client.API_URL = "https://testnet.binance.vision/api"

    print("Bot başladı...")

    while True:
        try:
            ticker = client.get_symbol_ticker(symbol=SYMBOL)
            price = float(ticker["price"])
            decision = simple_decision(price)

            print(f"Fiyat: {price} | Karar: {decision}")

            if decision == "BUY":
                order = client.create_order(
                    symbol=SYMBOL,
                    side="BUY",
                    type="MARKET",
                    quantity=TRADE_QTY
                )
                print("ALIM YAPILDI:", order["orderId"])
                time.sleep(60)

            time.sleep(5)

        except Exception as e:
            print("HATA:", e)
            time.sleep(10)

if __name__ == "__main__":
    main()
