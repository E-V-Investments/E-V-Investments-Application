import requests # TODO: Add requests to requirement.text
from Quotes.QuoteAPIProtocol import QuoteAPIProtocol
from Quotes.EnvironmentWrapper import EnvironmentVariable
from models.quote import Quote


class AlpacaWrapper(QuoteAPIProtocol):
    BASE_URL = "https://data.alpaca.markets/v2/stocks"
    # Do we want to include "stocks" in our "base url"? or have it as part of some url_path variable?

    def fetch_quote(self, symbol: str) -> Quote:
        url = f"{self.BASE_URL}/quotes/latest?symbols={symbol}"
        # and then should probably create a "url parameters" thing that stores symbols={symbol}
        # i'm thinking we do a request builder maybe, get some of this logic out of the get_quote method

        headers = {
            "APCA-API-KEY-ID": EnvironmentVariable()["ALPACA_API_KEY_ID"],
            "APCA-API-SECRET-KEY": EnvironmentVariable()["ALPACA_API_SECRET_KEY"]
        }

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