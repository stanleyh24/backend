from fastapi.exceptions import HTTPException
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database.database import get_db
from database import db_product
from typing import List
from .schemas import VariantBase, VariantDisplay, ProductBase, ProductDisplay

product = APIRouter(
    prefix='/products',
    tags=['Products']
)

@product.get('/',response_model=List[ProductDisplay])
def get_all_product(db:Session= Depends(get_db)):
    return db_product.get_all_product(db)

@product.get('/{product_id}', response_model=ProductDisplay)
def get_a_product(product_id : int, db:Session= Depends(get_db)):
    return db_product.get_one_product(db,product_id)

@product.post('/', response_model=ProductDisplay)
def create_product(request: ProductBase, db:Session= Depends(get_db)):
    return db_product.create_product(db,request)

@product.put('/{product_id}', response_model=ProductDisplay)
def update_product(product_id : int, request: ProductBase, db:Session= Depends(get_db)):
    return db_product.update_product(db, product_id, request)

@product.delete('/{product_id}')
def delete_product(product_id : int, db:Session= Depends(get_db)):
    return db_product.delete_product(db, product_id)

############### Variant ##################

@product.get('/{product_id}/variants', response_model=List[VariantDisplay])
def get_all_variants(product_id:int,db:Session= Depends(get_db)):
    return db_product.get_all_variant(db, product_id)

@product.get('/{product_id}/variant/{variant_id}', response_model=VariantDisplay)
def get_a_variant(product_id:int ,variant_id : int, db:Session= Depends(get_db)):
    return db_product.get_one_variant(db, product_id,variant_id)

@product.post('/{product_id}/variant',response_model=VariantDisplay)
def create_variant(request:VariantBase,db:Session= Depends(get_db)):
    return db_product.create_variant(db, request)

@product.put('/{product_id}/variant/{variant_id}', response_model=VariantDisplay)
def update_variant(product_id:int,variant_id : int,request:VariantBase ,db:Session= Depends(get_db)):
    return db_product.update_variant(db,product_id,variant_id,request)

@product.delete('/{product_id}/variant/{variant_id}')
def delete_variant(product_id:int,variant_id : int,db:Session= Depends(get_db)):
    return db_product.delete_variant(db,product_id,variant_id)