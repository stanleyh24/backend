from routers.schemas import ProductBase, VariantBase
from sqlalchemy.orm.session import Session
from database.models import Product, Variant
from datetime import datetime
from fastapi import HTTPException, status



def create_product(db:Session, request:ProductBase):
    new_product = Product(
        name= request.name,
        category_id= request.category_id,
        created_At= datetime.now()
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return  new_product

def get_all_product(db:Session):
    return db.query(Product).all()


def get_one_product(db:Session, product_id: int):
    if product := db.query(Product).filter(Product.id == product_id).first():
        return product
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Product with id {product_id} not found")


def update_product(db:Session, product_id: int, request:ProductBase):

    if not (product := db.query(Product).filter(Product.id == product_id).first()):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {product_id} not found")
    product.name= request.name
    product.category_id= request.category_id
    product.updated_At= datetime.now()
    db.commit()
    db.refresh(product)
    return product


def delete_product(db:Session, product_id: int):
    if not (product := db.query(Product).filter(Product.id == product_id).first()):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details=f"Product with id {product_id} not found")
    db.delete(product)
    db.commit()
    return 'ok'


############ Variant ############

def create_variant(db:Session, product_id:int,request:VariantBase):
    new_variant = Variant(
        name= request.name,
        length = request.length,
        diameter = request.diameter,
        strength = request.strength,
        packaging_type = request.packaging_type,
        price= request.price,
        product_id= product_id,
        available= request.available,
        created_At= datetime.now()
    )
    db.add(new_variant)
    db.commit()
    db.refresh(new_variant)
    return  new_variant

def get_all_variant(db:Session, product_id: int):
    return db.query(Variant).filter(Variant.product_id == product_id).all()


def get_one_variant(db:Session,product_id: int, variant_id: int):
    if variant := db.query(Variant).filter(Variant.product_id == product_id).filter(Variant.id == variant_id).first():
        return variant
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,details=f"Variant with id {variant_id} not found")


def update_variant(db:Session, product_id: int, variant_id: int, request:VariantBase):

    if not (variant := db.query(Variant).filter(Variant.product_id == product_id).filter(Variant.id == variant_id).first()):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details=f"variant with id {variant_id} not found")
    variant.name= request.name
    variant.length = request.length
    variant.diameter = request.diameter
    variant.strength = request.strength
    variant.packaging_type = request.packaging_type
    variant.price= request.price
    variant.product_id= product_id
    variant.available= request.available
    variant.updated_At= datetime.now()
    db.commit()
    db.refresh(variant)
    return variant


def delete_variant(db:Session,product_id: int, variant_id: int):
    if not (variant := db.query(Variant).filter(Variant.product_id == product_id).filter(Variant.id == variant_id).first()):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details=f"Variant with id {variant_id} not found")
    db.delete(variant)
    db.commit()
    return 'ok'