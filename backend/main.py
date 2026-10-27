
from fastapi import FastAPI
from controller.clientes import router as clientes_router
from controller.produtos import router as produtos_router

app = FastAPI(title="API Mercearia")

app.include_router(clientes_router)
app.include_router(produtos_router)
