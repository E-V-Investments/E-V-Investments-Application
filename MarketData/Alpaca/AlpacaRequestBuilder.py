# This class is responsible for building
#     * the full URL
#     * any query parameters
#     * (optionally) headers.
# This lets the AlpacaWrapper focus only on what it does — asking for a quote — while pushing the URL-building
# mechanics to a specialized class.
#
# The base URL and version are configurable. So if needed, you can do this:
# builder = AlpacaRequestBuilder(
#     base_url="https://sandbox-data.alpaca.markets",  # hypothetical dev environment
#     api_version="v3"  # or some future version
# )
# or just use the defaults:
# builder = AlpacaRequestBuilder()

from typing import Dict


class AlpacaRequestBuilder:
    def __init__(self, base_url: str = "https://data.alpaca.markets", api_version: str = "v2"):
        self.base_url = base_url.rstrip("/")  # Strip trailing slash to avoid double slashes in constructed URLs
        self.api_version = api_version.strip("/")  # Strip leading/trailing slashes just in case

    # This method returns an unambiguous string representation of the object, intended for developers.
    # It's especially helpful during debugging or when inspecting objects in logs or in the Python shell.
    #
    # Conventionally, it should look like valid Python code that could recreate the object.
    # For example:
    # >>> builder = AlpacaRequestBuilder()
    # >>> repr(builder)
    # "AlpacaRequestBuilder(base_url='https://data.alpaca.markets', api_version='v2')"
    def __repr__(self):
        return f"AlpacaRequestBuilder(base_url='{self.base_url}', api_version='{self.api_version}')"

    # This method returns a human-friendly string version of the object, intended for end users.
    # It’s used when you call print() on the object or use str() on it.
    # This version focuses on readability over technical precision.
    #
    # For example:
    # >>> builder = AlpacaRequestBuilder()
    # >>> print(builder)
    # Alpaca Request Builder (https://data.alpaca.markets/v2)
    def __str__(self):
        return f"Alpaca Request Builder ({self.base_url}/{self.api_version})"

    def build_latest_quote_url(self, symbol: str) -> str:
        endpoint_path = f"{self.api_version}/stocks/quotes/latest"
        query_string = f"symbols={symbol}"
        return f"{self.base_url}/{endpoint_path}?{query_string}"

    @staticmethod
    def build_headers(api_key: str, secret_key: str) -> Dict[str, str]:
        return {
            "APCA-API-KEY-ID": api_key,
            "APCA-API-SECRET-KEY": secret_key
        }