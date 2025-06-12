from fastapi import APIRouter, HTTPException, status
from app.schemas.usuario import UsuarioCreate
from app.service.usuario_service import registrar_novo_usuario

router = APIRouter()

@router.post("/register", status_code=status.HTTP_201_CREATED)
def registrar_usuario(usuario: UsuarioCreate):
    resultado = registrar_novo_usuario(usuario)
    if "erro" in resultado:
        raise HTTPException(status_code=400, detail=resultado["erro"])
    return resultado
