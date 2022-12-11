from routers.schemas import CategoryBase
from sqlalchemy.orm.session import Session
from database.models import Category
import datetime
from fastapi import HTTPException, status

def create(db:Session, request: CategoryBase):
    new_category = Category(
        name = request.name,
        created_At= datetime.datetime.now()

    )
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def get_all(db:Session):
    return db.query(Category).all()

def get_one(db:Session, category_id: int):
    category = db.query(Category).filter(Category.id == category_id).first()

    if not category:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f'Category with id {category_id} not found')
    
    return category

def update(db:Session, category_id: int, request: CategoryBase):
    category = db.query(Category).filter(Category.id == category_id).first()
    
    if not category:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f'Category with id {category_id} not found')
    
    category.name = request.name
    category.updated_At = datetime.datetime.now()
    db.commit()
    db.refresh(category)
    return category

def delete(db:Session, category_id: int):
    category = db.query(Category).filter(Category.id == category_id).first()

    if not category:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f'Category with id {category_id} not found')
    
    db.delete(category)
    db.commit()
    return 'ok'