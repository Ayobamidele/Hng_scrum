#!/usr/bin/env python3

"""Bitpay Service"""

from bitpay.client import Client, Environment, Facade, Invoice
from bitpay.models.invoice.buyer import Buyer
from api.utils.settings import settings
from api.v1.schemas.bitpay import CreateInvoice


class BitpayService:

    def __init__(self):
        """Initialize the service"""
        self.client = Client.create_pos_client(
            settings.BITPAY_API_TOKEN,
            Environment.TEST if settings.ENV == "dev" else Environment.PROD
        )

    def create_invoice(self, data: CreateInvoice):
        """Create a donation invoice"""
        invoice = Invoice()
        invoice.token = settings.BITPAY_API_TOKEN
        invoice.price = data.amount
        invoice.currency = data.currency
        invoice.notification_email = settings.NOTIFICATION_EMAIL
        invoice.notification_url = settings.NOTIFICATION_URL

        buyer = Buyer()
        buyer.email = data.email

        invoice.buyer = buyer
        return self.client.create_invoice(invoice, Facade.POS, False)

bitpay_service = BitpayService()
