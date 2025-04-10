import unittest
from Quotes.AlpacaRequestBuilder import AlpacaRequestBuilder


class TestAlpacaRequestBuilder(unittest.TestCase):
    def setUp(self):
        self.builder = AlpacaRequestBuilder(
            base_url="https://sandbox-data.alpaca.markets",
            api_version="v3"
        )

    def test_initializer_defaults(self):
        builder = AlpacaRequestBuilder()

        self.assertEqual(builder.base_url, "https://data.alpaca.markets")
        self.assertEqual(builder.api_version, "v2")

    def test_initializer_handles_trailing_and_leading_slashes(self):
        builder = AlpacaRequestBuilder(
            base_url="https://data.alpaca.markets/",
            api_version="/v2/"
        )
        expected = "https://data.alpaca.markets/v2/stocks/quotes/latest?symbols=AAPL"

        actual = builder.build_latest_quote_url("AAPL")

        assert actual == expected

    def test_repr(self):
        expected = "AlpacaRequestBuilder(base_url='https://sandbox-data.alpaca.markets', api_version='v3')"
        self.assertEqual(repr(self.builder), expected)

    def test_str(self):
        expected = "Alpaca Request Builder (https://sandbox-data.alpaca.markets/v3)"
        self.assertEqual(str(self.builder), expected)

    def test_build_headers(self):
        api_key = "fake-key"
        secret_key = "fake-secret"

        headers = self.builder.build_headers(api_key, secret_key)

        self.assertEqual(headers["APCA-API-KEY-ID"], api_key)
        self.assertEqual(headers["APCA-API-SECRET-KEY"], secret_key)
        self.assertEqual(len(headers), 2)

    def test_build_latest_quote_url(self):
        symbol = "AAPL"
        expected_url = "https://sandbox-data.alpaca.markets/v3/stocks/quotes/latest?symbols=AAPL"

        actual_url = self.builder.build_latest_quote_url(symbol)

        self.assertEqual(actual_url, expected_url)

    def test_build_latest_quote_url_with_lowercase_symbol(self):
        builder = AlpacaRequestBuilder()
        expected = "https://data.alpaca.markets/v2/stocks/quotes/latest?symbols=aapl"
        actual = builder.build_latest_quote_url("aapl")
        assert actual == expected

    def test_build_latest_quote_url_with_dot_symbol(self):
        builder = AlpacaRequestBuilder()
        expected = "https://data.alpaca.markets/v2/stocks/quotes/latest?symbols=BRK.B"
        actual = builder.build_latest_quote_url("BRK.B")
        assert actual == expected

    def test_build_latest_quote_url_with_empty_symbol(self):
        builder = AlpacaRequestBuilder()
        expected = "https://data.alpaca.markets/v2/stocks/quotes/latest?symbols="
        actual = builder.build_latest_quote_url("")
        assert actual == expected


if __name__ == "__main__":
    unittest.main()