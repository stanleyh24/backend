from database.database import get_db
from database.models import Order
from datetime import datetime

db = next(get_db())

order= db.query(Order).filter(Order.id=="0334b6fd-0d4f-4c03-b25a-f079a9d7e1a2").first()
order.paid=True
order.updated_At= datetime.now()
db.commit()

print(order.paid)