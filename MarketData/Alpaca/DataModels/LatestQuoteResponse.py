"""
This class models the response that gets returned from Alpaca's MarketData API's Stock / Latest quotes endpoint
https://docs.alpaca.markets/reference/stocklatestquotes-1
"""
from pydantic import BaseModel, Field
from typing import List, Dict

from MarketData.Alpaca.DataModels.Quote import Quote


class LatestQuoteResponse(BaseModel):
    quotes: Dict[str, Quote]