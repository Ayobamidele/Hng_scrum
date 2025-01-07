from pydantic import BaseModel, PositiveFloat , EmailStr


class DonationRequest(BaseModel):
    amount: PositiveFloat  # Amount in major currency unit (e.g., 10.50 for $10.50)
    currency: str  # ISO 4217 currency code (e.g., "USD", "EUR", "NGN")
    email: EmailStr  # Donor's email