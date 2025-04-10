import datetime
import requests
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
        self.assertEqual(
            result.timestamp,
            datetime.datetime(2025, 4, 4, 19, 59, 59, 874606, tzinfo=datetime.timezone.utc)
        )

    @patch("MarketData.MarketDataAPI.requests.get")
    def test_fetch_latest_quote_missing_symbol_raises(self, mock_get):
        # Arrange
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "quotes": {
                "TSLA": {  # Note: no "AAPL" here
                    "ap": 200,
                    "as": 5,
                    "ax": "V",
                    "bp": 195,
                    "bs": 3,
                    "bx": "V",
                    "c": ["R"],
                    "t": "2025-04-04T20:00:00.000000Z",
                    "z": "C"
                }
            }
        }
        mock_get.return_value = mock_response

        builder = AlpacaRequestBuilder()
        api = MarketDataAPI(secret_key="secret", api_key="key", builder=builder)

        # Act + Assert
        with self.assertRaises(ValueError) as context:
            api.fetch_latest_quote("AAPL")

        self.assertIn("No latest quote available for symbol: AAPL", str(context.exception))

    @patch("MarketData.MarketDataAPI.requests.get")
    def test_fetch_latest_quote_empty_response_raises(self, mock_get):
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

        self.assertIn("Failed to parse Alpaca response", str(context.exception))

    @patch("MarketData.MarketDataAPI.requests.get")
    def test_fetch_latest_quote_server_error_raises(self, mock_get):
        # Arrange
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.raise_for_status.side_effect = requests.HTTPError("Internal Server Error")
        mock_get.return_value = mock_response

        builder = AlpacaRequestBuilder()
        api = MarketDataAPI(secret_key="secret", api_key="key", builder=builder)

        # Act + Assert
        with self.assertRaises(requests.HTTPError) as context:
            api.fetch_latest_quote("AAPL")

        self.assertIn("Internal Server Error", str(context.exception))


if __name__ == "__main__":
    unittest.main()
