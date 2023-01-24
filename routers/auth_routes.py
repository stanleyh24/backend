from .schemas import UserModel, LoginModel
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT
from fastapi.encoders import jsonable_encoder
from werkzeug.security import check_password_hash
from fastapi.exceptions import HTTPException
from database.models import User

from database.database import get_db
from database import db_user


auth = APIRouter(
    prefix='/auth',
    tags=['auth']
)



@auth.post('/login', status_code=200 )
async def login(user : LoginModel, Authorize:AuthJWT=Depends(), db:Session= Depends(get_db)):
    db_user=db.query(User).filter(User.username==user.username).first()
    print(db_user)
    if db_user and check_password_hash(db_user.password, user.password):
        access_token=Authorize.create_access_token(subject=db_user.username)
        refresh_token=Authorize.create_refresh_token(subject=db_user.username)

        response={
            "access":access_token,
            "refresh":refresh_token
        }

        return jsonable_encoder(response)

    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
        detail="Invalid Username Or Password"
    )

@auth.post('/create_user', response_model=UserModel, status_code = status.HTTP_201_CREATED ) 
def create_user(user : UserModel, db:Session= Depends(get_db)):
    return db_user.create_user(db, user)

@auth.get('/refresh')
async def refresh_token(Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_refresh_token_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Please provide valid refresh token"
        ) from e
    current_user = Authorize.get_jwt_subject()
    access_token = Authorize.create_access_token(subject=current_user)
    return jsonable_encoder({"access":access_token})