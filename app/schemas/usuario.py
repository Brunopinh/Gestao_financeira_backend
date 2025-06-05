from pydantic import BaseModel, EmailStr
from datetime import date

class UsuarioCreate(BaseModel):
    nome: str
    email: EmailStr
    telefone: str
    login: str
    senha: str
    dt_nascimento: date
