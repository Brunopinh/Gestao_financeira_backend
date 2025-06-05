from app.schemas.usuario import UsuarioCreate
from app.crud.user_crud import criar_usuario

def registrar_novo_usuario(usuario: UsuarioCreate):
    # Aqui você pode validar, verificar se e-mail já existe, etc.
    return criar_usuario(usuario.nome, usuario.email, usuario.telefone, usuario.login, usuario.senha, usuario.dt_nascimento)
