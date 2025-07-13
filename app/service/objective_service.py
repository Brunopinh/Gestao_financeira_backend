from app.schemas.objective import ObjectiveCreate, ObjectiveUpdate, ObjectiveResponse
from app.crud.objective_crud import (criar_objetivo, listar_objetivos,
                                      atualizar_objetivo, excluir_objetivo)

def create_objective(objective: ObjectiveCreate): #criar um novo objetivo
    return criar_objetivo(objective.descricao, objective.vlr_objetivo, objective.dt_inicial, 
                          objective.dt_limite)

