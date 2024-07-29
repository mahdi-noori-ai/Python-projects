import requests
import time
import pandas as pd

def get_crypto_price_binance(symbol):
    """
    Function to get the current price of a specified cryptocurrency
    from the Binance API.

    Args:
    symbol (str): The symbol of the cryptocurrency (e.g., 'BTCUSDT').

    Returns:
    float: The current price of the cryptocurrency in USDT.
    """
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return float(data['price'])
    else:
        print("Error fetching data from Binance API")
        return None

def calculate_sma(prices, window):
    return pd.Series(prices).rolling(window=window).mean().iloc[-1]

def calculate_ema(prices, window):
    return pd.Series(prices).ewm(span=window, adjust=False).mean().iloc[-1]

def calculate_rsi(prices, window=14):
    delta = pd.Series(prices).diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi.iloc[-1]

if __name__ == "__main__":
    symbol = input("Enter the symbol of the cryptocurrency (e.g., 'BTCUSDT'): ").strip().upper()
    iterations = int(input("Enter the number of iterations: ").strip())
    interval = int(input("Enter the interval (in seconds) between each price fetch: ").strip())

    prices = []

    for i in range(iterations):
        price = get_crypto_price_binance(symbol)
        if price is not None:
            prices.append(price)
            if i > 0:
                price_change = prices[-1] - prices[-2]
                percentage_change = (price_change / prices[-2]) * 100
                sma = calculate_sma(prices, window=5)
                ema = calculate_ema(prices, window=5)
                rsi = calculate_rsi(prices, window=14) if len(prices) >= 14 else 'N/A'
                print(f"Iteration {i + 1}: The current price of {symbol} is ${price:.2f}, "
                      f"Price Change: ${price_change:.2f}, Percentage Change: {percentage_change:.2f}%, "
                      f"SMA(5): ${sma:.2f}, EMA(5): ${ema:.2f}, RSI(14): {rsi if rsi == 'N/A' else round(rsi, 2)}")
            else:
                print(f"Iteration {i + 1}: The current price of {symbol} is ${price:.2f}")
        time.sleep(interval)

    print("\nSummary of Changes:")
    for i in range(1, iterations):
        price_change = prices[i] - prices[i - 1]
        percentage_change = (price_change / prices[i - 1]) * 100
        print(f"Iteration {i + 1}: Price Change: ${price_change:.2f}, Percentage Change: {percentage_change:.2f}%")
