from Quotes.QuoteService import QuoteService
from Quotes.AlpacaWrapper import AlpacaWrapper


# print(QuoteService.fetch_quote(self=QuoteService, symbol="AAPL"))

alpaca_api = AlpacaWrapper()
quote_service = QuoteService(quote_api=alpaca_api)

quote = quote_service.fetch_quote("AAPL")
print(quote)
