from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
def fake_login(email: str):
    db = next(get_db())
    user = db.query(User).filter(User.email == email).first()
    if not user:
        user = User(email=email, is_paid=False)
        db.add(user)
        db.commit()
    return {"token": user.email}
def get_current_user(token: str = ""):
    db = next(get_db())
    user = db.query(User).filter(User.email == token).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user

