from fastapi import FastAPI
from app.core.config import add_cors_middleware

# Importa os routers da API
from app.api.v1.auth import login, register
from app.api.v1 import objective  # Certifique-se de que app/api/v1/objective.py existe e tem um router
from app.api.v1 import categoria  # Certifique-se de que app/api/v1/categoria.py existe e tem um router

app = FastAPI(
    title="Finanças API",
    description="API para implementar a regra dos dados",
    version="1.0.0"
)

# Adiciona o middleware de CORS
add_cors_middleware(app)

# Rotas 
# Inclui as rotas (endpoints)
app.include_router(register.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(login.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(objective.router, prefix="", tags=["Objective"])
app.include_router(categoria.router, prefix="/api/v1", tags=["Categoria"]) 




