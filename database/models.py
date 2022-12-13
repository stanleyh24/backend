from .database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship


class DateMixin():
    created_At = Column(DateTime)
    updated_At = Column(DateTime)
    


class Category(Base, DateMixin):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    product = relationship('Product', back_populates='category')


class Product(Base,DateMixin ):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    category_id = Column(Integer, ForeignKey("category.id"))
    variant = relationship('Variant', back_populates='product',cascade="all, delete",passive_deletes=True,)
    category = relationship('Category',  back_populates='product')


class Variant(Base,DateMixin):
    __tablename__ = 'variant'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    length = Column(String)
    diameter = Column(Float)
    strength = Column(String)
    packaging_type = Column(Integer)
    price = Column(Float)
    available = Column(Boolean)
    product_id = Column(Integer, ForeignKey("product.id"))
    product = relationship('Product', back_populates='variant')