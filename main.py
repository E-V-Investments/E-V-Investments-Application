from MarketData.AlpacaRequestBuilder import AlpacaRequestBuilder
from MarketData.Environment import Environment
from MarketData.QuoteService import QuoteService
from MarketData.AlpacaWrapper import AlpacaWrapper


env = Environment()
api_key = env.alpaca_api_key
secret_key = env.alpaca_secret_key
builder = AlpacaRequestBuilder()
api = AlpacaWrapper(api_key=api_key, secret_key=secret_key, builder=builder)

quote_service = QuoteService(quote_api=api)

quote = quote_service.fetch_quote("AAPL")
print(quote)
