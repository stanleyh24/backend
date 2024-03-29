from routers.schemas import OrderBase
from sqlalchemy.orm.session import Session
from database.models import Order, OrderDetail,Variant, Product
from datetime import datetime
import uuid

def create_order(db:Session, request:OrderBase):
    new_order = Order(
        id= str(uuid.uuid4()),
        number=1,
        first_name = request.first_name,
        last_name = request.last_name,
        email = request.email,
        phone = request.phone,
        country = request.country,
        address = request.address,
        postal_code = request.postal_code,
        city = request.city,
        amount=request.amount,
        shipping_type = request.shipping_type,
        shipping_price = request.shipping_price,
        total_amount = request.total_amount,
        created_At= datetime.now()
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    for product in request.products:
        order_detail = OrderDetail(
            id= str(uuid.uuid4()),
            order_id= new_order.id,
            variant_id= product.variant_id, 
            price = product.price,
            quantity= product.quantity,
            created_At= datetime.now()
        )
        db.add(order_detail)
    db.commit()

    return new_order


def get_orders(db:Session):
    return db.query(Order).all()

def get_order_details(db:Session, order_id):
    order_details=db.query(OrderDetail).filter(OrderDetail.order_id == order_id).all()
    products=[]
    
    for item in order_details:
        variant=db.query(Variant).filter(Variant.id == item.variant_id).first ()
        p = {
            'name': f"{variant.product.name} {variant.name} {variant.packaging_type}",
            'quantity':item.quantity,
            'price': item.price
        }
        products.append(p)
    
    return products
    
        