from pydantic import BaseModel
from datetime import date

class ObjectiveCreate(BaseModel):
    dt_inicial: date
    dt_limite: date
    vlr_objetivo: float
    descricao: str
    id_usuario: int
    
class ObjetivoUpdate(BaseModel):
    descricao: str
    dt_inicial: date
    dt_limite: date
    vlr_objetivo: float
    



