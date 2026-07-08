import yfinance as yf
from .yfinance_portal import get_history_data

def account_context_maker(account_password, first_name, last_name, username):
    return {
        "account_password": account_password,
        "first_name": first_name,
        "last_name": last_name,
        "username": username
    }

def stocks_context_maker(ticker: str, period: str = "1mo", interval: str = "1d"):
    stock = yf.Ticker(ticker)
    stock_info = stock.info
    hist_data = get_history_data(ticker, period, interval)
    print(hist_data)
    return {
        "title": "Stock API",
        "stock": stock_info,
        "hist_data": hist_data
    }
