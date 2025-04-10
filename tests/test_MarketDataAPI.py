import unittest
from unittest.mock import patch, MagicMock

from MarketData.Alpaca.AlpacaRequestBuilder import AlpacaRequestBuilder
from MarketData.MarketDataAPI import MarketDataAPI
from models.quote import Quote


class TestMarketDataAPI(unittest.TestCase):

    @patch("MarketData.MarketDataAPI.requests.get")
    def test_fetch_latest_quote_successful(self, mock_get):
        # Arrange
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
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
        }
        mock_get.return_value = mock_response

        builder = AlpacaRequestBuilder()
        market_data_api = MarketDataAPI(secret_key="secret-key", api_key="api-key", builder=builder)

        # Act
        result = market_data_api.fetch_latest_quote("AAPL")

        # Assert
        self.assertIsInstance(result, Quote)
        self.assertEqual(result.symbol, "AAPL")
        self.assertEqual(result.ask_price, 197.0)
        self.assertEqual(result.bid_price, 180.0)
        self.assertEqual(result.timestamp, "2025-04-04T19:59:59.874606332Z")

    @patch("MarketData.MarketDataAPI.requests.get")
    def test_fetch_latest_quote_raises_for_missing_quotes_key(self, mock_get):
        # Arrange
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response

        builder = AlpacaRequestBuilder()
        market_data_api = MarketDataAPI(secret_key="secret-key", api_key="api-key", builder=builder)

        # Act / Assert
        with self.assertRaises(ValueError) as context:
            market_data_api.fetch_latest_quote("AAPL")

        self.assertIn("No latest quote available for symbol", str(context.exception))

    @patch("MarketData.MarketDataAPI.requests.get")
    def test_fetch_latest_quote_raises_on_http_error(self, mock_get):
        # Arrange
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = Exception("HTTP Error")
        mock_get.return_value = mock_response

        builder = AlpacaRequestBuilder()
        market_data_api = MarketDataAPI(secret_key="secret-key", api_key="api-key", builder=builder)

        # Act / Assert
        with self.assertRaises(Exception) as context:
            market_data_api.fetch_latest_quote("AAPL")

        self.assertIn("HTTP Error", str(context.exception))


if __name__ == "__main__":
    unittest.main()
