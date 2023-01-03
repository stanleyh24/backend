from routers.schemas import OrderBase
from sqlalchemy.orm.session import Session
from database.models import Order, OrderDetail
from datetime import datetime
from fastapi import HTTPException, status
import uuid

def create_order(db:Session, request:OrderBase):
    new_order = Order(
        id= str(uuid.uuid4()),
        first_name = request.first_name,
        last_name = request.last_name,
        email = request.email,
        phone = request.phone,
        address = request.address,
        postal_code = request.postal_code,
        city = request.city,
        amount=request.amount,
        created_At= datetime.now()
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    for product in request.products:
        order_detail = OrderDetail(
            order_id= new_order.id,
            product_id= product.variant_id, 
            price = product.price,
            quantity= product.quantity,
            created_At= datetime.now()
        )
        db.add(order_detail)
    db.commit()

    return new_order
        