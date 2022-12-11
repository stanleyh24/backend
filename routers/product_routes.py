from fastapi import APIRouter

product = APIRouter(
    prefix='/products',
    tags=['Products']
)

@product.get('/')
def get_all_product():
    pass

@product.get('/{product_id}')
def get_a_product(product_id : int):
    pass

@product.post('/')
def create_product():
    pass

@product.put('/{product_id}')
def update_product(product_id : int):
    pass

@product.delete('/{product_id}')
def delete_product(product_id : int):
    pass


@product.get('/variants')
def get_all_variant():
    pass

@product.get('/variant/{variant_id}')
def get_a_variant(variant_id : int):
    pass

@product.post('/variant')
def create_variant():
    pass

@product.put('/variant/{variant_id}')
def update_variant(variant_id : int):
    pass

@product.delete('/variant/{variant_id}')
def delete_variant(variant_id : int):
    pass