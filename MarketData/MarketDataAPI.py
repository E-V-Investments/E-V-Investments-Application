import requests

from MarketData.Alpaca.AlpacaRequestBuilder import AlpacaRequestBuilder
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

        data = response.json()

        if "quotes" not in data:
            raise ValueError(f"No latest quote available for symbol: {symbol}")
        # i think we can do a better error message maybe

        quote_data = data["quotes"][symbol]
        ask_price = quote_data["ap"]
        bid_price = quote_data["bp"]
        timestamp = quote_data["t"]
        # we can put these strings into constants

        # should we add a convenience function called "create_quote_from_json"
        return Quote(
            symbol=symbol,
            ask_price=ask_price,
            bid_price=bid_price,
            timestamp=timestamp
        )

"""
SAMPLE GET QUOTE API RESPONSE
{
  "quotes": {
    "AAPL": {
      "ap": 197,
      "as": 10,
      "ax": "V",
      "bp": 180,
      "bs": 2,
      "bx": "V",
      "c": [
        "R"
      ],
      "t": "2025-04-04T19:59:59.874606332Z",
      "z": "C"
    }
  }
}"""