"""
The MarketDataAPIProtocol defines the methods that any market data provider must implement.

The `MarketDataService` can depend on any class implementing this protocol, forwarding its requests without needing to
know the underlying implementation. The protocol ensures that the class provides the necessary method(s), such as
`fetch_latest_quote`, to retrieve the latest market data for a given symbol.

By using this protocol, the `MarketDataService` remains decoupled from the specific details of the market data provider,
allowing for flexibility in changing or swapping the underlying API without affecting the service's functionality.
"""

from typing import Protocol
from models.quote import Quote


class MarketDataAPIProtocol(Protocol):
    def fetch_latest_quote(self, symbol: str) -> Quote:
        ...
