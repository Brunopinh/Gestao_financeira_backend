from fastapi import APIRouter, HTTPException # API criar grupo de rotas e HTTPE para erros (4004 ex)
from app.schemas.usuario import UsuarioLogin 
from app.service.login_service import autenticar_usuario
# 
router = APIRouter()

@router.post("/login")
def login(usuario: UsuarioLogin): 
    resultado = autenticar_usuario(usuario) # chama a autenticação
    if "erro" in resultado: #se caso tive erro na autenticação (401)
        raise HTTPException(status_code=401, detail=resultado["erro"])
    return resultado
