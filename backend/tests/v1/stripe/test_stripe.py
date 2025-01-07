import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
# from .v1.routes import stripe_donation  # Import your FastAPI app here
# from api.v1.services import stripe_service  # Import the actual service module
# from api.v1.routes import stripe_donation

from api.v1.routes import stripe_donation

client = TestClient(stripe_donation)

# Mock the create_checkout_session function
@pytest.fixture
def mock_create_checkout_session():
    """
    Mock the Stripe service's create_checkout_session function.
    """
    with patch("api.v1.services.stripe_service.create_checkout_session") as mock:
        mock.return_value = {
            "checkout_url": "https://checkout.stripe.com/session/test",
            "session_id": "cs_test_a1b2c3d4",
        }
        yield mock

# Mock the handle_success function
@pytest.fixture
def mock_handle_success():
    """
    Mock the Stripe service's handle_success function.
    """
    with patch("api.v1.services.stripe_service.handle_success") as mock:
        mock.return_value = {
            "status": "success",
            "customer_email": "test@example.com",
            "amount_total": 100.0,
        }
        yield mock

# Mock the success_response function
@pytest.fixture
def mock_success_response():
    """
    Mock the success_response function.
    """
    with patch("api.utils.success_response") as mock:
        mock.side_effect = lambda status, message, data: {
            "status_code": status,
            "message": message,
            "data": data,
        }
        yield mock

# Test for /donate endpoint
def test_create_donation_session(mock_create_checkout_session, mock_success_response):
    payload = {
        "amount": 10.0,
        "currency": "usd",
        "email": "donor@example.com",
    }

    response = client.post("/stripe/donate", json=payload)
    assert response.status_code == 200
    mock_create_checkout_session.assert_called_once_with(10.0, "usd", "donor@example.com")


# Test for /success/ endpoint
def test_success_endpoint(mock_handle_success, mock_success_response):
    session_id = "cs_test_a1b2c3d4"
    response = client.get(f"/stripe/success/?session_id={session_id}")

    assert response.status_code == 200
    mock_handle_success.assert_called_once_with(session_id)


# Test for /cancel/ endpoint
def test_cancel_endpoint(mock_success_response):
    response = client.get("/stripe/cancel/")

    assert response.status_code == 200