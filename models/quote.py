from dataclasses import dataclass


@dataclass
class Quote:
    symbol: str
    ask_price: float
    bid_price: float
    timestamp: str


