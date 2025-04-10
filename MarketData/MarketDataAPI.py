import requests

from MarketData.Alpaca.AlpacaRequestBuilder import AlpacaRequestBuilder
from MarketData.Alpaca.DataModels.LatestQuoteResponse import LatestQuoteResponse
from MarketData.MarketDataAPIProtocol import MarketDataAPIProtocol
from models.quote import Quote


class MarketDataAPI(MarketDataAPIProtocol):
    def __init__(self, api_key: str, secret_key: str, builder: AlpacaRequestBuilder):
        self.api_key = api_key
        self.secret_key = secret_key
        self.builder = builder

    def fetch_latest_quote(self, symbol: str) -> Quote:
        url = self.builder.build_latest_quote_url(symbol)
        headers = AlpacaRequestBuilder.build_headers(self.api_key, self.secret_key)

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print(response.text) # only for development purposes!

        # use Pydantic to validate + parse the full JSON
        try:
            parsed = LatestQuoteResponse.model_validate(response.json())
        except Exception as e:
            raise ValueError(f"Failed to parse Alpaca response: {e}")

        if symbol not in parsed.quotes:
            raise ValueError(f"No latest quote available for symbol: {symbol}")

        # Convert to our app-level Quote model (not the raw API quote)
        return Quote.from_alpaca(symbol, parsed.quotes[symbol])

