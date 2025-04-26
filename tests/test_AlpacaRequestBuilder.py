import unittest
from MarketData.Alpaca.AlpacaRequestBuilder import AlpacaRequestBuilder


class TestAlpacaRequestBuilder(unittest.TestCase):

    # <editor-fold desc="Initializer Tests">

    def test_initializer_defaults(self):
        # Act
        builder = AlpacaRequestBuilder()

        # Assert
        self.assertEqual(builder.base_url, "https://data.alpaca.markets")
        self.assertEqual(builder.api_version, "v2")

    def test_initializer_handles_trailing_and_leading_slashes(self):
        # Arrange
        base_url_with_unnecessary_trailing_slash = "https://la.dee.da/"
        api_version_with_unnecessary_leading_and_trailing_slashes = "/v100/"

        # Act
        builder = AlpacaRequestBuilder(
            base_url=base_url_with_unnecessary_trailing_slash,
            api_version=api_version_with_unnecessary_leading_and_trailing_slashes
        )

        # Assert
        self.assertEqual(builder.base_url, "https://la.dee.da")
        self.assertEqual(builder.api_version, "v100")

    def test_initializer_handles_multiple_trailing_and_leading_slashes(self):
        # Arrange
        base_url_with_unnecessary_trailing_slash = "https://la.dee.da///"
        api_version_with_unnecessary_leading_and_trailing_slashes = "//v100////"

        # Act
        builder = AlpacaRequestBuilder(
            base_url=base_url_with_unnecessary_trailing_slash,
            api_version=api_version_with_unnecessary_leading_and_trailing_slashes
        )

        # Assert
        self.assertEqual(builder.base_url, "https://la.dee.da")
        self.assertEqual(builder.api_version, "v100")

    # </editor-fold>

    # <editor-fold desc="Magic Method Tests">

    def test_repr(self):
        # Arrange
        builder = AlpacaRequestBuilder(
            base_url="https://la.dee.da",
            api_version="v100"
        )

        # Act
        output_string = repr(builder)

        # Assert
        expected = "AlpacaRequestBuilder(base_url='https://la.dee.da', api_version='v100')"
        self.assertEqual(output_string, expected)

    def test_str(self):
        # Arrange
        builder = AlpacaRequestBuilder(
            base_url="https://la.dee.da",
            api_version="v100"
        )

        # Act
        output_string = str(builder)

        # Assert
        expected = "Alpaca Request Builder (https://la.dee.da/v100)"
        self.assertEqual(output_string, expected)

    # </editor-fold>

    # <editor-fold desc="build_headers() Tests">

    def test_build_headers(self):
        # Arrange
        builder = AlpacaRequestBuilder()
        api_key = "fake-key"
        secret_key = "fake-secret"

        # Act
        headers = builder.build_headers(api_key, secret_key)

        # Assert
        self.assertEqual(headers["APCA-API-KEY-ID"], api_key)
        self.assertEqual(headers["APCA-API-SECRET-KEY"], secret_key)
        self.assertEqual(len(headers), 2)

    # </editor-fold>

    # <editor-fold desc="build_latest_quote_url() Tests">

    def test_build_latest_quote_url(self):
        # Arrange
        builder = AlpacaRequestBuilder(
            base_url="https://la.dee.da",
            api_version="v100"
        )
        symbol = "AAPL"

        # Act
        url = builder.build_latest_quote_url(symbol)

        # Assert
        expected_url = "https://la.dee.da/v100/stocks/quotes/latest?symbols=AAPL"
        self.assertEqual(url, expected_url)

    def test_build_latest_quote_url_with_lowercase_symbol(self):
        # Arrange
        builder = AlpacaRequestBuilder(
            base_url="https://la.dee.da",
            api_version="v100"
        )
        symbol = "aapl"

        # Act
        url = builder.build_latest_quote_url(symbol)

        # Assert
        expected_url = "https://la.dee.da/v100/stocks/quotes/latest?symbols=aapl"
        self.assertEqual(url, expected_url)

    def test_build_latest_quote_url_with_dot_symbol(self):
        # Arrange
        builder = AlpacaRequestBuilder(
            base_url="https://la.dee.da",
            api_version="v100"
        )
        symbol = "AAP.L"

        # Act
        url = builder.build_latest_quote_url(symbol)

        # Assert
        expected_url = "https://la.dee.da/v100/stocks/quotes/latest?symbols=AAP.L"
        self.assertEqual(url, expected_url)

    def test_build_latest_quote_url_with_empty_symbol(self):
        # Arrange
        builder = AlpacaRequestBuilder(
            base_url="https://la.dee.da",
            api_version="v100"
        )
        symbol = ""

        # Act
        url = builder.build_latest_quote_url(symbol)

        # Assert
        expected_url = "https://la.dee.da/v100/stocks/quotes/latest?symbols="
        self.assertEqual(url, expected_url)

    # </editor-fold>

if __name__ == "__main__":
    unittest.main()