#!/usr/bin/env python3


from pydantic import BaseModel
from api.v1.schemas.base_schema import ResponseBase


class CreateInvoice(BaseModel):
    """Create invoice input"""
    price: float
    currency: str = "USD"


class CreateInvoiceResponse(ResponseBase):
    """Create payment response model"""
    data: str
