#!/usr/bin/env python3

"""Bitpay API donation routes"""


from fastapi import APIRouter, status

from api.utils.response import success_response
from api.v1.schemas.bitpay import CreateInvoice, CreateInvoiceResponse
from api.v1.services.bitpay import bitpay_service

bitpay_donation = APIRouter(prefix="/bitpay", tags=["Bitpay", "Donation"])


@bitpay_donation.post(
    "",
    response_model=CreateInvoiceResponse,
    status_code=status.HTTP_200_OK
)
def create_invoice(req: CreateInvoice):
    """Create a Bitpay invoice"""
    try:
        invoice = bitpay_service.create_invoice(req)

        return success_response(
            status_code=status.HTTP_200_OK,
            message="Invoice created successfully",
            data={
                "donation_url": invoice.url
            }
        )
    except Exception as e:
        return success_response(
            status_code=status.HTTP_400_BAD_REQUEST,
            message=str(e)
        )
