from fastapi import APIRouter, status
from database import Session, ENGINE
from schemas import OrderModel


order_router = APIRouter(prefix="/orders", tags=["Orders"])
session = Session(bind=ENGINE)


@order_router.get("/orders")
async def get_orders():
    orders = session.query(OrderModel).all()
    return orders