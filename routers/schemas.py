from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from typing import List

class CategoryBase(BaseModel):
    name : str
        
    class Config():
        orm_mode= True

class CategoryDisplay(BaseModel):
    id: int
    name : str
    created_At: datetime
    updated_At: datetime | None

    class Config():
        orm_mode= True


class ProductBase(BaseModel):
    name: str
    category_id: int

    class Config():
        orm_mode= True

class ProductDisplay(BaseModel):
    id: int
    name: str
    category_id: int

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
    id: int
    name: str
    length: str
    diameter: float
    strength: str
    packaging_type: int
    price:float
    product_id: int
    available: bool


    class Config():
        orm_mode= True