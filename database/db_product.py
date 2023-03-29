from routers.schemas import ProductBase, VariantBase
from sqlalchemy.orm.session import Session
from database.models import Product, Variant, Category
from datetime import datetime
from fastapi import HTTPException, status
import uuid
from utils.utils import slugify


def create_product(db:Session, request:ProductBase):
    new_product = Product(
        id= str(uuid.uuid4()),
        name= request.name,
        description= request.description,
        slug = slugify(request.name),
        image_url= request.image_url,
        category_id= request.category_id,
        created_At= datetime.now()
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return  new_product

def get_all_product(category: str, db:Session):
    if category is None :
        return db.query(Product).all()
    
    c = db.query(Category).filter(Category.slug == category).first()
    return db.query(Product).filter(Product.category_id == c.id).all()


def get_one_product(db:Session, product_id: str ):
    if product := db.query(Product).filter(Product.id == product_id).first():
        return product
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Product with id {product_id} not found")

def get_by_category(db: Session, category_slug:str):
    category = db.query(Category).filter(Category.slug == category_slug).first()
    print(category)
    if products := db.query(Product).filter(Product.category_id == category.id):
        return products


def update_product(db:Session, product_id: str, request:ProductBase):

    if not (product := db.query(Product).filter(Product.id == product_id).first()):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {product_id} not found")
    product.name= request.name
    slug = slugify(request.name)
    product.category_id= request.category_id
    product.updated_At= datetime.now()
    db.commit()
    db.refresh(product)
    return product


def delete_product(db:Session, product_id: str):
    if not (product := db.query(Product).filter(Product.id == product_id).first()):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details=f"Product with id {product_id} not found")
    db.delete(product)
    db.commit()
    return 'ok'


############ Variant ############

def create_variant(db:Session, product_id:str,request:VariantBase):
    new_variant = Variant(
        id= str(uuid.uuid4()),
        name= request.name,
        slug = slugify(request.name),
        length = request.length,
        diameter = request.diameter,
        strength = request.strength,
        packaging_type = request.packaging_type,
        price= request.price,
        product_id= product_id,
        available= request.available,
        packaging_length = request.packaging_length, 
        packaging_width = request.packaging_width, 
        packaging_height = request.packaging_height,
        created_At= datetime.now()
    )
    db.add(new_variant)
    db.commit()
    db.refresh(new_variant)
    return  new_variant

def get_all_variant(db:Session, product_id: str):
    return db.query(Variant).filter(Variant.product_id == product_id).all()


def get_one_variant(db:Session,product_id: str, variant_id: str):
    if variant := db.query(Variant).filter(Variant.product_id == product_id).filter(Variant.id == variant_id).first():
        return variant
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,details=f"Variant with id {variant_id} not found")


def update_variant(db:Session, product_id: str, variant_id: str, request:VariantBase):

    if not (variant := db.query(Variant).filter(Variant.product_id == product_id).filter(Variant.id == variant_id).first()):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details=f"variant with id {variant_id} not found")
    variant.name= request.name
    slug = slugify(request.name)
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


def delete_variant(db:Session,product_id: str, variant_id: str):
    if not (variant := db.query(Variant).filter(Variant.product_id == product_id).filter(Variant.id == variant_id).first()):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details=f"Variant with id {variant_id} not found")
    db.delete(variant)
    db.commit()
    return 'ok'