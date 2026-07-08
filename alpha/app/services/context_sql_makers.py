import yfinance as yf
from .yfinance_portal import get_history_data

def account_context_sql_maker(account_password: str, first_name: str, last_name: str, username: str):
    return {
        "title": "Stock API", 
        "account_password": account_password,
        "username": username,
        "last_name": last_name,
        "first_name": first_name,
    }

def stocks_context_sql_maker(ticker: str, period: str = "1mo", interval: str = "1d"):
    stock = yf.Ticker(ticker)
    stock_info = stock.info
    hist_data = get_history_data(ticker, period, interval)
    print(hist_data)
    return {
        "title": "Stock API",
        "stock": stock_info,
        "hist_data": hist_data
    }
