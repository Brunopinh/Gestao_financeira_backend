# core/cors.py
from fastapi.middleware.cors import CORSMiddleware

def add_cors_middleware(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3001", "http://192.168.0.68:3000", "http://qa.onereport.com:3000", "http://172.23.214.19:3001", "http://localhost:3000","http://100.76.211.19:3000"],  # Endereços do frontend
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
