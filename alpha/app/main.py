import yfinance as yf
from pathlib import Path
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from .services.yfinance_portal import *
from .services.context_makers import *
from .database.database_management import engine, Base
from .database.update_tables import *
from .models.tables import *

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Stock Data API",
    description="An API to fetch stock data using yfinance",
    version="1.0.0",
)

BASE_DIR = Path(__file__).resolve().parent
print(f"BASE_DIR: {BASE_DIR}")
templates = Jinja2Templates(
    directory=str(BASE_DIR / "front_end/")
)

print(f"BASE_DIR: {str(BASE_DIR / "front_end")}")

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "front_end" / "static"),
    name="static"
)

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={
        "title": "Stock API"
    }
)

@app.get("/stocks")
def show_stock_data(request: Request, ticker: str = "AAPL"):
    context_ = stocks_context_maker(ticker)
    return templates.TemplateResponse(
    request=request,
    name="stocks_data.html",
    context=context_
)

@app.get("/account")
def show_account_detail(request: Request,):
    return templates.TemplateResponse(
    request=request,
    name="account.html",
    context={}
)

@app.post("/account")
def create_account(
    request: Request,
    username: str = Form(...),
    first_name: str = Form(...),
    last_name: str = Form(...),
    email: str = Form(...),
    account_password: str = Form(...)
):
    context = account_context_maker(
        account_password,
        first_name,
        last_name,
        email,
        username,
    )
    
    update_user_table(context)

    return templates.TemplateResponse(
        request=request,
        name="account.html",
        context=context,
    )

def main():
    ticker = input("Enter the stock ticker symbol (e.g., AAPL, MSFT): ")
    try:
        stock_info = get_stock_data(ticker)
        print_stock_info(stock_info)
    except Exception as e:
        print(f"Exception catched: {e}")

if __name__ == "__main__":
    main()
