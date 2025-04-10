from MarketData.MarketDataAPIProtocol import MarketDataAPIProtocol
from models.quote import Quote


class MarketDataService:
    def __init__(self, market_data_api: MarketDataAPIProtocol):
        self.market_data_api = market_data_api

    def fetch_quote(self, symbol: str) -> Quote:
        return self.market_data_api.fetch_quote(symbol)
