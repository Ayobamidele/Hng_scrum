#!/usr/bin/env python3


from pydantic import BaseModel
from api.v1.schemas.base_schema import ResponseBase


class CreateInvoice(BaseModel):
    """Create invoice input"""
    amount: float
    currency: str = "USD"
    email: str


class CreateInvoiceResponse(ResponseBase):
    """Create payment response model"""
    data: str
