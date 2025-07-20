from pydantic import BaseModel
from typing import Literal

class CategoriaCreate(BaseModel):
    tp_movimentacao: Literal['E', 'S']
    descricao: str

class CategoriaUpdate(BaseModel):
    tp_movimentacao: Literal['E', 'S']
    descricao: str
