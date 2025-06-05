from fastapi import APIRouter, HTTPException


router = APIRouter()


@router.post("/login")
def login(usuario: UsuarioLogin):
    token = autenticar_usuario(usuario)
    if not token:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    return {"access_token": token, "token_type": "bearer"}