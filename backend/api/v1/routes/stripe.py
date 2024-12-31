import stripe
from fastapi import HTTPException, Request, APIRouter
from api.utils import success_response

stripe_donation = APIRouter(prefix="/stripe", tags=["Todos"])


@stripe_donation.post("/create-payment-intent")
async def create_payment_intent(request: Request):
    try:
        body = await request.json()
        amount = body.get("amount")  
        if not amount:
            raise HTTPException(status_code=400, detail="Amount is required")

        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency="usd",
            payment_method_types=["card", "bank_transfer"], 
        )
        return success_response(
                status_code=200,
                message="Payment intent created successfully",
                data={"clientSecret": payment_intent["client_secret"]}
            )
    except Exception as e:
        return success_response(
                status_code=400,
                message=e.msg,
                data={"error": str(e)}
            )


@stripe_donation.post("/webhook")
async def stripe_webhook():
    # Psuedo code 
    return success_response(
       status_code=200,
       message="Webhook received"
    )
