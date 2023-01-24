from fastapi.exceptions import HTTPException
from fastapi import APIRouter, Depends, status, File, UploadFile
from sqlalchemy.orm import Session
import random
import string
import shutil

from database.database import get_db
from database import db_product
from typing import List
from .schemas import VariantBase, VariantDisplay, ProductBase, ProductDisplay

from utils.utils import confirm_payment

product = APIRouter(
    prefix='/products',
    tags=['Products']
)

@product.get('/',response_model=List[ProductDisplay])
async def get_all_product(category: str | None = None, db:Session= Depends(get_db)):
    return db_product.get_all_product(category,db)

@product.get('/{product_id}', response_model=ProductDisplay)
def get_a_product(product_id : str, db:Session= Depends(get_db)):
    return db_product.get_one_product(db,product_id)


@product.post('/', response_model=ProductDisplay, status_code = status.HTTP_201_CREATED )
def create_product(request: ProductBase,db:Session= Depends(get_db),):
    return db_product.create_product(db,request)

@product.put('/{product_id}', response_model=ProductDisplay)
def update_product(product_id : int, request: ProductBase, db:Session= Depends(get_db)):
    return db_product.update_product(db, product_id, request)

@product.delete('/{product_id}')
def delete_product(product_id : str, db:Session= Depends(get_db)):
    return db_product.delete_product(db, product_id)

@product.post('/image')
def upload_image(image: UploadFile = (...)):
    letters = string.ascii_letters
    rand_str = ''.join(random.choice(letters) for _ in range(6))
    new= f'_{rand_str}.'
    filename = new.join(image.filename.rsplit('.', 1))
    path = f'images/{filename}'

    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {'filemane': path}

############### Variant ##################

@product.get('/{product_id}/variants', response_model=List[VariantDisplay])
def get_all_variants(product_id:str,db:Session= Depends(get_db)):
    return db_product.get_all_variant(db, product_id)

@product.get('/{product_id}/variant/{variant_id}', response_model=VariantDisplay)
def get_a_variant(product_id:str ,variant_id : str, db:Session= Depends(get_db)):
    return db_product.get_one_variant(db, product_id,variant_id)

@product.post('/{product_id}/variant',response_model=VariantDisplay, status_code = status.HTTP_201_CREATED )
def create_variant(product_id:str,request:VariantBase,db:Session= Depends(get_db)):
    return db_product.create_variant(db,product_id, request)

@product.put('/{product_id}/variant/{variant_id}', response_model=VariantDisplay)
def update_variant(product_id:str,variant_id : str,request:VariantBase ,db:Session= Depends(get_db)):
    return db_product.update_variant(db,product_id,variant_id,request)

@product.delete('/{product_id}/variant/{variant_id}')
def delete_variant(product_id:str,variant_id : str,db:Session= Depends(get_db)):
    return db_product.delete_variant(db,product_id,variant_id)