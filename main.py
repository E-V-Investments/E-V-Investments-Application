from Quotes.AlpacaRequestBuilder import AlpacaRequestBuilder
from Quotes.Environment import Environment
from Quotes.QuoteService import QuoteService
from Quotes.AlpacaWrapper import AlpacaWrapper


env = Environment()
api_key = env.alpaca_api_key
secret_key = env.alpaca_secret_key
builder = AlpacaRequestBuilder()
api = AlpacaWrapper(api_key=api_key, secret_key=secret_key, builder=builder)

quote_service = QuoteService(quote_api=api)

quote = quote_service.fetch_quote("AAPL")
print(quote)
