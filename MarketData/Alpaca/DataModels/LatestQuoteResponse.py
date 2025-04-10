from pydantic import BaseModel, Field
from typing import List, Dict

from MarketData.Alpaca.DataModels.Quote import Quote


class LatestQuoteResponse(BaseModel):
    quotes: Dict[str, Quote]