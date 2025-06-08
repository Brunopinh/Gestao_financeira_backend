from fastapi import APIRouter, HTTPException
from app.schemas.usuario import UsuarioLogin
from app.service.login_service import autenticar_usuario

router = APIRouter()

@router.post("/login")
def login(usuario: UsuarioLogin):
    resultado = autenticar_usuario(usuario)
    if "erro" in resultado:
        raise HTTPException(status_code=401, detail=resultado["erro"])
    return resultado
