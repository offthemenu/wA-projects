from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Wireframe

router = APIRouter(prefix="/v01")