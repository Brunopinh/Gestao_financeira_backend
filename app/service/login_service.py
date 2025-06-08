from app.schemas.usuario import UsuarioLogin
from app.crud.user_crud import autenticacao_usuario

def autenticar_usuario(usuario: UsuarioLogin):
    return autenticacao_usuario(usuario.login, usuario.senha)
