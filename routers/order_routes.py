from fastapi.exceptions import HTTPException
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database.database import get_db
from database import db_order
from typing import List
from .schemas import OrderBase, OrderResponse, OrderDisplay
from fastapi_jwt_auth import AuthJWT

order = APIRouter(
    prefix='/orders',
    tags=['Orders']
)

@order.post('/', response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
def create_order(request: OrderBase, db:Session= Depends(get_db)):
    return db_order.create_order(db, request)

@order.get('', response_model=List[OrderDisplay], status_code=status.HTTP_200_OK)
def get_order(db:Session= Depends(get_db),Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token"
        ) from e
    return db_order.get_orders(db)


