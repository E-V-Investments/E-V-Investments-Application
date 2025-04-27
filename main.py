from MarketData.Alpaca.AlpacaRequestBuilder import AlpacaRequestBuilder
from MarketData.Environment import Environment
from MarketData.MarketDataService import MarketDataService
from MarketData.MarketDataAPI import MarketDataAPI


env = Environment()
api_key = env.alpaca_api_key
secret_key = env.alpaca_secret_key
builder = AlpacaRequestBuilder()
api = MarketDataAPI(api_key=api_key, secret_key=secret_key, builder=builder)

market_data_service = MarketDataService(market_data_api=api)

latets_quote_for_apple = market_data_service.fetch_latest_quote("AAPL")
print(latets_quote_for_apple)

latest_quote_for_tesla = market_data_service.fetch_latest_quote("TSLA")
print(latest_quote_for_tesla)

latest_quote_for_google = market_data_service.fetch_latest_quote("GOOG")
print(latest_quote_for_google)

latest_quote_for_alphabet = market_data_service.fetch_latest_quote("GOOGL")
print(latest_quote_for_alphabet)
