from pydantic import BaseModel, EmailStr
from datetime import date  #datetime biblioteca para de data 
 
class UsuarioCreate(BaseModel):   #criação de usuario, chama a API (os dados precisar ser fornecidos)
    nome: str   #str texto
    email: EmailStr
    telefone: str
    login: str
    senha: str
    dt_nascimento: date

class UsuarioLogin(BaseModel):
    login: str
    senha: str
