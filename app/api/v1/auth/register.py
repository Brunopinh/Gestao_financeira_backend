<<<<<<< HEAD
from fastapi import APIRouter, HTTPException, status
from app.schemas.usuario import UsuarioCreate
=======
from fastapi import APIRouter, HTTPException, status #HTTP ERROR Personalizados (400,401,404)
from app.schemas.usuario import UsuarioCreate #espera receber os dados do usuario para criar
>>>>>>> 325f06a (VersaoQuatro)
from app.service.usuario_service import registrar_novo_usuario

router = APIRouter()

<<<<<<< HEAD
@router.post("/register", status_code=status.HTTP_201_CREATED)
def registrar_usuario(usuario: UsuarioCreate):
=======
@router.post("/register", status_code=status.HTTP_201_CREATED) #depois que alguem fazer uma requição POST, ele retorna que foi criado com sucesso
def registrar_usuario(usuario: UsuarioCreate): #formato schames (de acordo com o foi definido USUARIOCREATE)
>>>>>>> 325f06a (VersaoQuatro)
    resultado = registrar_novo_usuario(usuario)
    if "erro" in resultado:
        raise HTTPException(status_code=400, detail=resultado["erro"]) 
    return resultado