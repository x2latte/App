from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal
import models.models as models
import schemas.schemas as schemas

router = APIRouter()

# Dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/categories/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    db_category = models.Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

@router.get("/categories/", response_model=List[schemas.Category])
def list_categories(db: Session = Depends(get_db)):
    return db.query(models.Category).all()