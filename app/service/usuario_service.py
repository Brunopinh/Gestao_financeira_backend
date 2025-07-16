from app.schemas.usuario import UsuarioCreate
from app.crud.user_crud import criar_usuario
from app.crud.user_crud import get_user_by_email, get_user_by_cpf

def registrar_novo_usuario(usuario: UsuarioCreate):
    usuario_existente = get_user_by_email(usuario.email)
    usuario_existente_cpf = get_user_by_cpf(usuario.cpf)
    if usuario_existente:
        return {"erro": "E-mail já cadastrado"}
    if usuario_existente_cpf:
        return {"erro": "CPF já cadastrado"}
    # Aqui você pode validar, verificar se e-mail já existe, etc.
    return criar_usuario(usuario.nome, usuario.email, usuario.telefone, usuario.login, usuario.senha, usuario.dt_nascimento, usuario.cpf)
