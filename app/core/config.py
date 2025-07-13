# core/cors.py  #configurações do front end para se conectar com o back
from fastapi.middleware.cors import CORSMiddleware

def add_cors_middleware(app): #M: Permite ou bloqueia o acesso de outros dominios.
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3001", "http://localhost:5173","http://127.0.0.1:5173/"],  # Endereços do frontend
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
