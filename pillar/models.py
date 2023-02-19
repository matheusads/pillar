from enum import Enum
from typing import Optional

from pydantic import BaseModel, constr


class Order(str, Enum):
    asc = "asc"
    desc = "desc"


class RequestModel(BaseModel):
    words: list[constr(strict=True)]
    order: Optional[Order] = Order.asc

    class Config:
        use_enum_values = True
