from Quotes.AlpacaRequestBuilder import AlpacaRequestBuilder
from Quotes.EnvironmentWrapper import EnvironmentVariable
from Quotes.QuoteService import QuoteService
from Quotes.AlpacaWrapper import AlpacaWrapper


api_key = EnvironmentVariable()("ALPACA_API_KEY_ID")
secret_key = EnvironmentVariable()("ALPACA_API_SECRET_KEY")
builder = AlpacaRequestBuilder()
api = AlpacaWrapper(api_key=api_key, secret_key=secret_key, builder=builder)

quote_service = QuoteService(quote_api=api)

quote = quote_service.fetch_quote("AAPL")
print(quote)
