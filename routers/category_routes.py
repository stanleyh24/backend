
from fastapi.exceptions import HTTPException
from fastapi import APIRouter, Depends, status
from fastapi_jwt_auth import AuthJWT
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
def get_a_category(category_id : str,db:Session= Depends(get_db) ):
    return db_category.get_one(db, category_id)


@category.post('/', response_model=CategoryDisplay,status_code = status.HTTP_201_CREATED)
def create_category(request: CategoryBase, db:Session= Depends(get_db), Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token"
        ) from e
    return db_category.create(db,request)

@category.put('/{category_id}', response_model=CategoryDisplay)
def update_category(category_id : str, request: CategoryBase, db:Session=Depends(get_db)):
    return db_category.update(db, category_id, request)

@category.delete('/{category_id}')
def delete_category(category_id : str, db:Session=Depends(get_db)):
    return db_category.delete(db, category_id)