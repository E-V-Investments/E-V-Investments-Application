from dataclasses import dataclass
from datetime import datetime

from MarketData.Alpaca.DataModels.Quote import Quote as AlpacaQuote

@dataclass
class Quote:
    symbol: str
    ask_price: float
    bid_price: float
    timestamp: datetime

    @classmethod
    def from_alpaca(cls, symbol: str, alpaca_quote: AlpacaQuote) -> "Quote":
        return cls(
            symbol=symbol,
            ask_price=alpaca_quote.ap,
            bid_price=alpaca_quote.bp,
            timestamp=alpaca_quote.t,
        )


