from pydantic import BaseModel
from typing import List


class StockInfo(BaseModel):
    ticker: str
    name: str
    sector: str
    industry: str
    market_cap: float
    pe_ratio: float
    dividend_yield: float
    price: float


class StockData(BaseModel):
    dates: List[str]
    prices: List[float]


class Stock(BaseModel):
    info: StockInfo
    data: StockData
    

class AccountDetail(BaseModel):
    account_password: str
    first_name: str
    last_name: str
    username: str
