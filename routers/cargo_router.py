from fastapi import APIRouter, status
from database import Session, ENGINE
from schemas import CargoModel
from http import HTTPStatus
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi.exceptions import HTTPException


cargo_router = APIRouter(prefix="/cargo", tags=["Cargo"])
session = Session(bind=ENGINE)


@cargo_router.get("/orders")
async def get_cargo():
    cargo = session.query(CargoModel).all()
    return cargo

