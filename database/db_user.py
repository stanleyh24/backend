from database.models import User
from routers.schemas import UserModel, LoginModel
from sqlalchemy.orm.session import Session
from datetime import datetime
from werkzeug.security import generate_password_hash , check_password_hash
import uuid


def create_user(db:Session, request:UserModel):
    new_user = User(
        id = str(uuid.uuid4()),
        username= request.username,
        name = request.name,
        last_name = request.last_name,
        email = request.email,
        password=  generate_password_hash(request.password),
        is_staff= request.is_staff,
        is_active=request.is_active,
        created_At= datetime.now()
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def login(db:Session, user:LoginModel):
    pass
