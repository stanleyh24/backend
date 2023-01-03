from fastapi import APIRouter, Request,status, BackgroundTasks
from utils.utils import confirm_payment

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


