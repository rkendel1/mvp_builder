from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Artifact
from services.claude import generate_mvp_code
from services.auth_utils import get_current_user, get_db
router = APIRouter()
@router.post("/generate")
def generate_artifact(idea: str, db: Session = Depends(get_db), user=Depends(get_current_user)):
    if not user.is_paid and user.quota_used >= 1:
        raise HTTPException(402, detail="Upgrade required.")
code = generate_mvp_code(idea)
artifact = Artifact(
        user_id=user.id,
        title="Generated MVP",
        idea_input=idea,
        claude_prompt=idea,
        output_html=code,
        is_paid_only=True
    )
    db.add(artifact)
    user.quota_used += 1
    db.commit()
return {"html": code}
@router.get("/my")
def list_artifacts(user=Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(Artifact).filter(Artifact.user_id == user.id).all()
