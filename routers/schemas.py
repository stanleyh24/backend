from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from typing import List

class CategoryBase(BaseModel):
    name : str
        
    class Config():
        orm_mode= True

class CategoryDisplay(BaseModel):
    id: str
    name : str
    slug : str
    created_At: datetime
    updated_At: datetime | None

    class Config():
        orm_mode= True


class ProductBase(BaseModel):
    name: str
    category_id: str
    image_url:str

    class Config():
        orm_mode= True

class ProductDisplay(BaseModel):
    id: str
    name: str
    slug : str
    image_url:str
    category_id: str

    class Config():
        orm_mode= True


class VariantBase(BaseModel):
    name: str
    length: str
    diameter: float
    strength: str
    packaging_type: int
    price:float
    available: bool

    class Config():
        orm_mode= True

class VariantDisplay(BaseModel):
    id: str
    name: str
    slug : str
    length: str
    diameter: float
    strength: str
    packaging_type: int
    price:float
    product_id: str
    available: bool


    class Config():
        orm_mode= True

class OrderDetail(BaseModel):
    variant_id: str
    price:float
    quantity: int

class OrderBase(BaseModel):
    first_name:str
    last_name:str
    email:str
    phone:str
    address:str
    postal_code :str
    city:str
    products:List[OrderDetail]
    amount:float

    class Config():
        orm_mode= True

class OrderResponse(BaseModel):
    id: str
    amount:float

    class Config():
        orm_mode= True