
from fastapi.exceptions import HTTPException
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database.database import get_db
from database import db_category
from typing import List
from .schemas import CategoryBase, CategoryDisplay

category = APIRouter(
    prefix='/categories',
    tags=['Categories']
)

@category.get('/', response_model=List[CategoryDisplay])
def get_all_category(db:Session= Depends(get_db)):
    return db_category.get_all(db)

@category.get('/{category_id}', response_model=CategoryDisplay)
def get_a_category(category_id : int,db:Session= Depends(get_db) ):
    return db_category.get_one(db, category_id)


@category.post('/', response_model=CategoryDisplay)
def create_category(request: CategoryBase, db:Session= Depends(get_db)):
    return db_category.create(db,request)

@category.put('/{category_id}', response_model=CategoryDisplay)
def update_category(category_id : int, request: CategoryBase, db:Session=Depends(get_db)):
    return db_category.update(db, category_id, request)

@category.delete('/{category_id}')
def delete_category(category_id : int, db:Session=Depends(get_db)):
    return db_category.delete(db, category_id)