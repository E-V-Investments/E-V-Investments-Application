from typing import Protocol
from models.quote import Quote


class MarketDataAPIProtocol(Protocol):
    def fetch_latest_quote(self, symbol: str) -> Quote:
        ...
