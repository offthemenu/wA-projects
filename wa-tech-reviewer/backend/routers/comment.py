from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Comment, Wireframe
from pydantic import BaseModel
from typing import List
from datetime import datetime

router = APIRouter(prefix="/v01")

class CommentSchema(BaseModel):
    project: str
    device: str
    page_name: str
    page_path: str
    ui_component: str
    comment: str

class CommentOut(CommentSchema):
    created_at: datetime

    class Config:
        orm_mode = True

def get_db():
    """
    FastAPI dependency to provide a database session.

    Yields a database session that should be used as a context manager.
    The session is closed after the context manager is exited.
    """
    db = SessionLocal()
    try:
        print("Database session is being closed.")
        yield db
    finally:
        db.close()

@router.post("/add_comment")
def add_comment(payload: CommentSchema, db: Session = Depends(get_db)):

    wireframe = db.query(Wireframe).filter_by(page_name = payload.page_name).first()
    
    if not wireframe:
        raise ValueError(f"No wireframe found for page_name: {payload.page_name}")

    # Step 2: Create new Comment with wireframe_id set
    new_comment = Comment(**payload.model_dump(), wireframe_id=wireframe.id)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

@router.get("/comments", response_model=List[CommentOut])
def get_all_comments(db: Session = Depends(get_db)):
    results = db.query(Comment).order_by(Comment.created_at.desc()).all()
    return results