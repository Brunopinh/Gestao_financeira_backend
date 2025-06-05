from fastapi import FastAPI
from app.core.config import add_cors_middleware

# Importa os routers da API
from app.api.v1.auth import login, register

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



