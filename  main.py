from fastapi import FastAPI
from app.database import engine, Base
from app.routes import products, categories, brands, images
import app.models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Internet Shop API")

app.include_router(products.router)
app.include_router(categories.router)
app.include_router(brands.router)
app.include_router(images.router)