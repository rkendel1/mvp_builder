from fastapi import APIRouter
from services.stripe_utils import create_checkout
router = APIRouter()
@router.post("/checkout")
def stripe_checkout(email: str):
    return create_checkout(email)

