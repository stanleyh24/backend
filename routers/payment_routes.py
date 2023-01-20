from fastapi import APIRouter, Request, status, BackgroundTasks, Depends
from sqlalchemy.orm import Session
from utils.utils import confirm_payment, create_invoice
from database.database import get_db

payment = APIRouter(
    prefix='/payment',
    tags=['Payment']
)


@payment.post('/paypal', status_code=status.HTTP_200_OK)
async def get_payment(request:Request, background_tasks: BackgroundTasks):
    headers=request.headers
    body= await request.json()
    background_tasks.add_task(confirm_payment, headers=headers, body=body)
    return {"message":"ok"}


@payment.get('/invoice', status_code=status.HTTP_200_OK)
async def get_payment(background_tasks: BackgroundTasks):
    background_tasks.add_task(create_invoice,order_id="0334b6fd-0d4f-4c03-b25a-f079a9d7e1a2")
    return {"message":"ok"}


