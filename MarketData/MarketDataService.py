from MarketData.QuoteAPIProtocol import QuoteAPIProtocol
from models.quote import Quote


class MarketDataService:
    def __init__(self, quote_api: QuoteAPIProtocol):
        self.quote_api = quote_api

    def fetch_quote(self, symbol: str) -> Quote:
        return self.quote_api.fetch_quote(symbol)
