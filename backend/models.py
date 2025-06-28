from sqlalchemy import Column, Integer, String, ForeignKey, Text, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    is_paid = Column(Boolean, default=False)
    quota_used = Column(Integer, default=0)
class Artifact(Base):
    __tablename__ = "artifacts"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String)
    idea_input = Column(Text)
    claude_prompt = Column(Text)
    output_html = Column(Text)
    is_paid_only = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
user = relationship("User", backref="artifacts")

