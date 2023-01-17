from fastapi.exceptions import HTTPException
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database.database import get_db
from database import db_order
from typing import List
from .schemas import OrderBase, OrderResponse

order = APIRouter(
    prefix='/orders',
    tags=['Orders']
)

@order.post('/', response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
def create_order(request: OrderBase, db:Session= Depends(get_db)):
    return db_order.create_order(db, request)


