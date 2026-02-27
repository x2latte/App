from pydantic import BaseModel
from typing import List, Optional

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    class Config:
        orm_mode = True

class BrandBase(BaseModel):
    name: str

class BrandCreate(BrandBase):
    pass

class Brand(BrandBase):
    id: int
    class Config:
        orm_mode = True

class ProductImageBase(BaseModel):
    url: str

class ProductImageCreate(ProductImageBase):
    pass

class ProductImage(ProductImageBase):
    id: int
    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    category_id: int
    brand_id: int

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    images: List[ProductImage] = []
    category: Category
    brand: Brand
    class Config:
        orm_mode = True