from fastapi import APIRouter, Depends, HTTPException
from services.auth_utils import fake_login, get_current_user
router = APIRouter()
@router.post("/login")
def login(email: str):
    return fake_login(email)
@router.get("/me")
def me(user=Depends(get_current_user)):
    return {"email": user.email, "is_paid": user.is_paid}
