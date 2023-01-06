from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from database import models
from database.database  import engine
from fastapi.middleware.cors import CORSMiddleware
from fastapi_jwt_auth import AuthJWT
from routers import category_routes, product_routes, order_routes,payment_routes, auth_routes
from dotenv import load_dotenv
from routers.schemas import Settings



app= FastAPI(title="Caoba Cigars API")

@AuthJWT.load_config
def get_config():
    return Settings()

@app.get("/")
async def root():
    return {"message": "Hello World"}
app.include_router(auth_routes.auth)
app.include_router(category_routes.category)
app.include_router(product_routes.product)
app.include_router(order_routes.order)
app.include_router(payment_routes.payment)

models.Base.metadata.create_all(engine)

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount('/images', StaticFiles(directory='images'),name='images')

load_dotenv()
