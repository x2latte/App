from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app.schemas.product import ProductCreate, ProductResponse
from app.services.pagination import paginate
from typing import List

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", response_model=ProductResponse)
def create_product(data: ProductCreate, db: Session = Depends(get_db)):
    product = models.Product(**data.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


@router.get("/", response_model=List[ProductResponse])
def get_products(page: int = 1, limit: int = 10, search: str = "", db: Session = Depends(get_db)):
    query = db.query(models.Product)

    if search:
        query = query.filter(models.Product.name.contains(search))

    products = paginate(query, page, limit).all()
    return products


@router.put("/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, data: ProductCreate, db: Session = Depends(get_db)):
    product = db.get(models.Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    for key, value in data.model_dump().items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)
    return product


@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.get(models.Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product)
    db.commit()
    return {"detail": "Deleted"}