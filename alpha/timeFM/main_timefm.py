from app.services.yfinance_portal import get_history_data

a = get_history_data("AAPL", "1mo", "1d")
print(a)
