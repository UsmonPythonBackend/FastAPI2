from fastapi import APIRouter
from database import Session, ENGINE
from schemas import ProductModel


product_router = APIRouter(prefix="/products", tags=["Products"])
session = Session(bind=ENGINE)


@product_router.get("/orders")
async def get_products():
    products = session.query(ProductModel).all()
    return products