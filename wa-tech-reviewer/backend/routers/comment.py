from fastapi import APIRouter, Depends, HTTPException
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
    filename: str

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
def add_comment(comment_data: CommentSchema, db: Session = Depends(get_db)):
    wireframe_record = db.query(Wireframe).filter_by(page_name=comment_data.page_name).first()
    if not wireframe_record:
        raise HTTPException(status_code=400, detail="No wireframe found for that page")

    new_comment = Comment(**comment_data.model_dump(), wireframe_id=wireframe_record.id)
    db.add(new_comment)

    try:
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Failed to add comment: {e}")
    
    db.refresh(new_comment)
    return new_comment
    

@router.get("/comments", response_model=List[CommentOut])
def get_all_comments(db: Session = Depends(get_db)):
    try:
        results = db.query(Comment).order_by(Comment.created_at.desc()).all()
        return results
    except Exception as e:
        print(f"[ERROR] Failed to get comments: {e}")
        raise HTTPException(status_code=400, detail="Failed to get comments")
