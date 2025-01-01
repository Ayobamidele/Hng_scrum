from fastapi import  APIRouter
from api.utils import success_response

stripe_donation = APIRouter(prefix="/stripe", tags=["Stripe", "Donation"])


@stripe_donation.post("/product")
async def create_product(name: str):
    return success_response(
        200,
        f"{name} Product Created Successfully",
        {}
    )
