import yfinance as yf

def get_stock_data(ticker: str):
    ticker_data = yf.Ticker(ticker)
    stock_info = ticker_data.info
    return stock_info

def print_stock_info(stock_info):
    print("--------------------------------------")
    print(stock_info["shortName"])
    print("--------------------------------------")
    print("\n\n\n")

def get_formatted_stock_data(ticker: str):
    stock_info = get_stock_data(ticker)
    formatted_data = {
        "ticker": stock_info.get("symbol", ""),
        "name": stock_info.get("shortName", ""),
        "sector": stock_info.get("sector", ""),
        "industry": stock_info.get("industry", ""),
        "market_cap": stock_info.get("marketCap", 0.0),
        "pe_ratio": stock_info.get("trailingPE", 0.0),
        "dividend_yield": stock_info.get("dividendYield", 0.0),
        "price": stock_info.get("regularMarketPrice", 0.0),
    }
    
    return formatted_data

def create_stock_class(ticker: str):
    try:
        stock_info = get_formatted_stock_data(ticker)
        from models.models import StockData
        stock_data_instance = StockData(**stock_info)
        return stock_data_instance
    except Exception as e:
        print(f"Error creating StockData instance: {e}")
        return None

def get_history_data(ticker: str = "AAPL", period: str = "1mo", interval: str = "1d"):
    ticker_data = yf.Ticker(ticker)
    history_data = ticker_data.history(
        period=period,
        interval=interval
    )
    history_data.reset_index(inplace=True)
    history_data = history_data[["Date", "Close"]]
    history_data["Date"] = history_data["Date"].dt.strftime("%Y-%m-%d")
    return history_data.to_dict(orient="records")