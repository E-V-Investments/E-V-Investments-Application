from MarketData.AlpacaRequestBuilder import AlpacaRequestBuilder
from MarketData.Environment import Environment
from MarketData.MarketDataService import MarketDataService
from MarketData.AlpacaWrapper import AlpacaWrapper


env = Environment()
api_key = env.alpaca_api_key
secret_key = env.alpaca_secret_key
builder = AlpacaRequestBuilder()
api = AlpacaWrapper(api_key=api_key, secret_key=secret_key, builder=builder)

market_data_service = MarketDataService(market_data_api=api)

quote = market_data_service.fetch_quote("AAPL")
print(quote)
