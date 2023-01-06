from .database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float, Text
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship



class DateMixin():
    created_At = Column(DateTime,nullable=False)
    updated_At = Column(DateTime)
    
class User(Base, DateMixin):
    __tablename__ = 'user'
    id = Column(String, primary_key=True, index=True)
    username = Column(String, nullable=False)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String(80),nullable=False)
    password=Column(Text,nullable=True)
    is_staff=Column(Boolean,default=False)
    is_active=Column(Boolean,default=False)

class Category(Base, DateMixin):
    __tablename__ = 'category'
    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    slug= Column(String(100), nullable=False)
    product = relationship('Product', back_populates='category')


class Product(Base,DateMixin ):
    __tablename__ = 'product'
    id = Column(String, primary_key=True, index=True)
    name = Column(String,nullable=False)
    description = Column(String(), nullable=False)
    image_url= Column(String, nullable=False)
    slug= Column(String(100), nullable=False)
    category_id = Column(Integer, ForeignKey("category.id"),nullable=False)
    variant = relationship('Variant', back_populates='product',cascade="all, delete",passive_deletes=True)
    category = relationship('Category',  back_populates='product')


class Variant(Base,DateMixin):
    __tablename__ = 'variant'
    id = Column(String, primary_key=True, index=True)
    name = Column(String,nullable=False)
    slug= Column(String(100), nullable=False)
    length = Column(String,nullable=False)
    diameter = Column(Float,nullable=False)
    strength = Column(String,nullable=False)
    packaging_type = Column(Integer,nullable=False)
    price = Column(Float,nullable=False)
    available = Column(Boolean)
    product_id = Column(Integer, ForeignKey("product.id"),nullable=False)
    product = relationship('Product', back_populates='variant')


class Order(Base,DateMixin):
    __tablename__ = 'order'
    id = Column(String, primary_key=True, index=True)
    first_name = Column(String,nullable=False)
    last_name = Column(String,nullable=False)
    email = Column(String,nullable=False)
    phone = Column(String,nullable=False)
    address = Column(String,nullable=False)
    postal_code = Column(String,nullable=False)
    city = Column(String,nullable=False)
    amount=Column(Float,nullable=False)
    paid = Column(Boolean,default=False)

    items = relationship('OrderDetail', back_populates="order", cascade="all, delete",passive_deletes=True)

class OrderDetail(Base,DateMixin):
    __tablename__ = 'order_datail'
    id = Column(String, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("order.id"),nullable=False)
    product_id = Column(Integer, ForeignKey("product.id"),nullable=False)
    price = Column(Float,nullable=False)
    quantity = Column(Integer,default=1)

    order = relationship("Order", back_populates="items")