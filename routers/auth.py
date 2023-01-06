from fastapi import APIRouter
from .schemas import UserBase
from auth.auth import write_token

auth_routes = APIRouter()



@auth_routes.post('/login')
def login(user : UserBase):
    return write_token(user.dict())