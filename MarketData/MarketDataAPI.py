"""
The MarketDataAPI class abstracts communication with the Alpaca API for market data. It is used by the MarketDataService
to fetch financial data, interpret the API response, and return data in a format suitable for the service.

This class insulates the MarketDataService from changes to the Alpaca API, meaning that if Alpaca's API changes, only
this class needs to be modified. Similarly, if we choose to switch from Alpaca to another financial service provider,
the MarketDataService remains unaffected.

This class exposes methods like `fetch_latest_quote`, which retrieves the most recent quote for a given symbol and
returns it as a `Quote` object.
"""

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
            latest_quote_response = LatestQuoteResponse.model_validate(response.json())
        except Exception as e:
            raise ValueError(f"Failed to parse Alpaca response: {e}")

        quotes_dictionary = latest_quote_response.quotes
        if symbol not in quotes_dictionary:
            raise ValueError(f"No latest quote available for symbol: {symbol}")

        # Convert to our app-level Quote model (not the raw API quote)
        alpaca_quote = quotes_dictionary[symbol]
        our_quote_model = Quote.from_alpaca(symbol, alpaca_quote)
        return our_quote_model

