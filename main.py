from fastapi import FastAPI
from database import models
from database.database  import engine
from routers import category_routes, product_routes

app= FastAPI(title="Caoba Cigars API")

app.include_router(category_routes.category)
app.include_router(product_routes.product)

@app.get("/")
async def root():
    return {"message": "Hello World"}


models.Base.metadata.create_all(engine)