# Bitcoin Price Tracker

Welcome to the Bitcoin Price Tracker project! This repository contains a Python script to track the price of Bitcoin using the Binance API. you can use this script to collect Bitcoin price data for various data analysis and machine learning projects.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Functionality](#functionality)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project provides a script to track the price of Bitcoin in real-time using the Binance API. The script fetches the current price of Bitcoin and can be extended to log the data over time for analysis or model training.

## Installation

To get started with the project, clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/bitcoin-price-tracker.git
cd bitcoin-price-tracker
pip install -r requirements.txt
```

### Setting Up a Virtual Environment

It is recommended to use a virtual environment to manage dependencies. Here's how you can set it up:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

To use the script, run the following command:

```bash
python BTC-price-tracker.py
```

### Example Usage in Script

You can also import the `get_crypto_price_binance` function into your Python script and use it as follows:

```python
from BTC_price_tracker import get_crypto_price_binance

symbol = 'BTCUSDT'
price = get_crypto_price_binance(symbol)
print(f"The current price of {symbol} is {price} USDT")
```

## Functionality

The script uses the `requests` library to send HTTP requests to the Binance API and retrieve the current price of Bitcoin. Here's a brief overview of the main function:

```python
import requests

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
        print(f"Error fetching data: {response.status_code}")
        return None
```

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
