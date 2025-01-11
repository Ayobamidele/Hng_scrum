#!/usr/bin/env python3
"""Unittest for bitpay donations"""
from fastapi import status
import pytest
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch

from api.v1.routes import bitpay_donation
from api.v1.schemas.bitpay import CreateInvoice

client = TestClient(bitpay_donation)

@pytest.fixture
def mock_create_invoice():
    """
    Mock the bitpay service's create_invoice function.
    """
    with patch("api.v1.services.bitpay_service.create_invoice") as mock:
        invoice_mock = Mock()
        invoice_mock.url = "https://test.bitpay.com/invoice/invoice-id"
        mock.return_value = invoice_mock
        yield mock


def test_create_invoice(mock_create_invoice):
    payload = {
        "amount": 20,
        "currency": "usd",
        "email": "donor@example.com",
    }

    response = client.post("/bitpay", json=payload)
    assert response.status_code == 200
    mock_create_invoice.assert_called_once_with(
        CreateInvoice(amount=20, currency="usd", email="donor@example.com"))

