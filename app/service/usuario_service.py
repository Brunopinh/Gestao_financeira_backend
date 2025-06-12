from app.schemas.usuario import UsuarioCreate
from app.crud.user_crud import criar_usuario
from app.crud.user_crud import get_user_by_email

def registrar_novo_usuario(usuario: UsuarioCreate):
    usuario_existente = get_user_by_email(usuario.email)
    if usuario_existente:
        return {"erro": "E-mail já cadastrado"}
    # Aqui você pode validar, verificar se e-mail já existe, etc.
    return criar_usuario(usuario.nome, usuario.email, usuario.telefone, usuario.login, usuario.senha, usuario.dt_nascimento)
