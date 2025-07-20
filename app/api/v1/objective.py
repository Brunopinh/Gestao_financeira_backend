from fastapi import APIRouter, Depends
from app.crud import objective_crud
from app.schemas.objective import ObjectiveCreate, ObjetivoUpdate
from app.crud.objective_crud import obter_usuario_logado


router = APIRouter()


@router.get("/objetivos/") # Lista todos os objetivos
def listar_objetivos():
    return objective_crud.listar_objetivos()

@router.post("/objetivos/") # Cria um novo objetivo
def criar_objetivo(objetivo: ObjectiveCreate):  
    return objective_crud.criar_objetivo(
        objetivo.descricao,
        objetivo.vlr_objetivo,
        objetivo.dt_inicial,
        objetivo.dt_limite,
        objetivo.id_usuario
    )


@router.put("/objetivos/{objetivo_id}") # Atualiza um objetivo existente
def atualizar_objetivo(
    objetivo_id: int,
    objetivo: ObjetivoUpdate,
    usuario: dict = Depends(obter_usuario_logado)
):
    return objective_crud.atualizar_objetivo(
        id_objetivo=objetivo_id,
        descricao=objetivo.descricao,
        vlr_objetivo=objetivo.vlr_objetivo,
        dt_inicial=objetivo.dt_inicial,
        dt_limite=objetivo.dt_limite,
        id_usuario=usuario["id"]  # Ultimo parametro esperado
    )


@router.delete("/objetivos/{id_objetivo}") # Exclui um objetivo
def excluir_objetivo(id_objetivo: int):
    objective_crud.excluir_objetivo(id_objetivo)
    return {"mensagem": "Objetivo excluído com sucesso"}