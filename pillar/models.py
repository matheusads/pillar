from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, constr


class Order(str, Enum):
    asc = "asc"
    desc = "desc"


class RequestModel(BaseModel):
    words: List[constr(strict=True)]
    order: Optional[Order] = Order.asc

    class Config:
        use_enum_values = True
