import stripe
import os
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
def create_checkout(email: str):
    session = stripe.checkout.Session.create(
        customer_email=email,
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": "usd",
                "product_data": {
                    "name": "MVP Pro Plan",
                },
                "unit_amount": 4900,
            },
            "quantity": 1,
        }],
        mode="subscription",
        success_url="http://localhost:5173/success",
        cancel_url="http://localhost:5173/cancel",
    )
    return {"url": session.url}

