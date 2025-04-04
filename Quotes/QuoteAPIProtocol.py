from typing import Protocol
from models.quote import Quote


class QuoteAPIProtocol(Protocol):
    def get_quote(self, symbol: str) -> Quote:
        ...
