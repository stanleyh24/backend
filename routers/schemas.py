from typing import List, Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List




class Settings(BaseModel):
    authjwt_secret_key:str='b4bb9013c1c03b29b9311ec0df07f3b0d8fd13edd02d5c45b2fa7b86341fa405'

class LoginModel(BaseModel):
    username: str
    password:str

    
class UserModel(BaseModel):
    id:Optional[str]
    username:str
    name: str
    last_name : str
    email: EmailStr
    password:str
    is_staff:Optional[bool]
    is_active:Optional[bool]


    class Config:
        orm_mode=True
        schema_extra={
            'example':{
                "username":"johndoe",
                "name": "john",
                "last_name": "doe",
                "email":"johndoe@gmail.com",
                "password":"password",
                "is_staff":False,
                "is_active":True
            }
        }

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
    description: str
    category_id: str
    image_url:str

    class Config():
        orm_mode= True

class ProductDisplay(BaseModel):
    id: str
    name: str
    description: str
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
    packaging_length:float
    packaging_width:float
    packaging_height:float
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
    packaging_length:float
    packaging_width:float
    packaging_height:float


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
    country:str
    address:str
    postal_code :str
    city:str
    products:List[OrderDetail]
    amount:float
    shipping_type: str
    shipping_price:float
    total_amount:float
    


    class Config():
        orm_mode= True

class OrderResponse(BaseModel):
    id: str
    amount:float

    class Config():
        orm_mode= True


class ShipTo(BaseModel):
    Name: str
    AddressLine: str
    City: str
    PostalCode: str
    CountryCode: str
    
    class Config():
        orm_mode= True