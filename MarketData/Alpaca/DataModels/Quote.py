from pydantic import BaseModel, Field
from typing import List
from datetime import datetime


class Quote(BaseModel):
    #should i put these in alphabetical order?
    ap: float  # ask price
    bp: float  # bid price
    as_: int = Field(alias="as")  # ask size (alias because 'as' is a keyword)
    bs: int  # bid size
    ax: str # wut dis
    bx: str # wut dis
    c: List[str]
    t: datetime  # timestamp, will be auto-parsed from ISO 8601
    z: str

    model_config = {
        "populate_by_name": True,  # allows using as_ when parsing
        "extra": "ignore"  # ignore unexpected keys if any - Erin, change this
    }


"""
SAMPLE GET LATEST QUOTE API RESPONSE
{
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
}"""