from fastapi import APIRouter
from app.crud import objective_crud
from app.schemas.objective import ObjectiveCreate


router = APIRouter()


@router.get("/objetivos/")
def listar_objetivos():
    return objective_crud.listar_objetivos()

@router.post("/objetivos/")
def criar_objetivo(objetivo: ObjectiveCreate):  
    return objective_crud.criar_objetivo(
        objetivo.descricao,
        objetivo.vlr_objetivo,
        objetivo.dt_inicial,
        objetivo.dt_limite,
        objetivo.id_usuario

    )

@router.put("/objetivos/{objetivo_id}")
def atualizar_objetivo(objetivo_id: int, objetivo: ObjectiveCreate):
    return objective_crud.atualizar_objetivo(
        objetivo_id,
        objetivo.descricao,
        objetivo.vlr_objetivo,
        objetivo.dt_inicial,
        objetivo.dt_limite
    )

@router.delete("/objetivos/{id_objetivo}")
def excluir_objetivo(id_objetivo: int):
    return objective_crud.excluir_objetivo(id_objetivo)