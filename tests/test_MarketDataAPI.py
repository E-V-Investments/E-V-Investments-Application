import unittest
from unittest.mock import patch, MagicMock
from MarketData.MarketDataAPI import MarketDataAPI
from models.quote import Quote


class TestMarketDataAPI(unittest.TestCase):

    @patch("MarketData.MarketDataAPI.EnvironmentVariable")
    @patch("MarketData.MarketDataAPI.requests.get")
    def test_fetch_quote_successful(self, mock_get, mock_env):
        # Arrange
        mock_env_instance = MagicMock()
        mock_env_instance.return_value = "mock_key"
        mock_env.return_value = mock_env_instance

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "quotes": {
                "AAPL": {
                    "ap": 197.0,
                    "bp": 180.0,
                    "t": "2025-04-04T19:59:59.874606332Z"
                }
            }
        }
        mock_get.return_value = mock_response

        market_data_api = MarketDataAPI()

        # Act
        result = market_data_api.fetch_quote("AAPL")

        # Assert
        self.assertIsInstance(result, Quote)
        self.assertEqual(result.symbol, "AAPL")
        self.assertEqual(result.ask_price, 197.0)
        self.assertEqual(result.bid_price, 180.0)
        self.assertEqual(result.timestamp, "2025-04-04T19:59:59.874606332Z")

    @patch("MarketData.MarketDataAPI.EnvironmentVariable")
    @patch("MarketData.MarketDataAPI.requests.get")
    def test_fetch_quote_raises_for_missing_quotes_key(self, mock_get, mock_env):
        # Arrange
        mock_env_instance = MagicMock()
        mock_env_instance.return_value = "mock_key"
        mock_env.return_value = mock_env_instance

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response

        market_data_api = MarketDataAPI()

        # Act / Assert
        with self.assertRaises(ValueError) as context:
            market_data_api.fetch_quote("AAPL")

        self.assertIn("No latest quote available for symbol", str(context.exception))

    @patch("MarketData.MarketDataAPI.EnvironmentVariable")
    @patch("MarketData.MarketDataAPI.requests.get")
    def test_fetch_quote_raises_on_http_error(self, mock_get, mock_env):
        # Arrange
        mock_env_instance = MagicMock()
        mock_env_instance.return_value = "mock_key"
        mock_env.return_value = mock_env_instance

        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = Exception("HTTP Error")
        mock_get.return_value = mock_response

        market_data_api = MarketDataAPI()

        # Act / Assert
        with self.assertRaises(Exception) as context:
            market_data_api.fetch_quote("AAPL")

        self.assertIn("HTTP Error", str(context.exception))


if __name__ == "__main__":
    unittest.main()
