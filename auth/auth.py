from jwt import encode, decode
from jwt import exceptions
from datetime import datetime, timedelta
from os import getenv
from fastapi.responses import JSONResponse

def expire_date(days: int):
    date= datetime.now()
    return date + timedelta(days)
    


def write_token(data: dict):
    return encode(payload={**data,"exp": expire_date(2)}, key=getenv("SECRET_KEY"), algorithm="HS256")


def validate_token(token, output=False):
    try:
        if output:
            decode(token, key=getenv("SECRET_KEY"), algorithms=["HS256"])
        decode(token, key=getenv("SECRET_KEY"), algorithms=["HS256"])
    except exceptions.DecodeError:
        return JSONResponse(content={"message": "Invalid Token"}, status_code=401)
    except exceptions.ExpiredSignatureError:
        return JSONResponse(content={"message": "Token Expired"}, status_code=401)