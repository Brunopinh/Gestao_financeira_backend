from pydantic import BaseModel, EmailStr, Field
from datetime import date
import re

class UsuarioCreate(BaseModel):
    nome: str
    email: EmailStr
    telefone: str
    login: str = Field(..., min_length=1)
    senha: str = Field(..., min_length=6)
    dt_nascimento: date
    cpf: str = Field(..., pattern=r'^\d{3}\.?\d{3}\.?\d{3}\-?\d{2}$')  # CPF deve ter 11 dígitos

class UsuarioLogin(BaseModel):
    login: str
    senha: str