from fastapi import APIRouter, Depends, HTTPException
from app.crud import categoria_crud
from app.schemas.categoria import CategoriaCreate


router = APIRouter()

@router.get("/categorias/")
def listar_categorias():
    return categoria_crud.listar_categorias()

@router.post("/categorias/")
def criar_categoria(categoria: CategoriaCreate):
    resultado = categoria_crud.criar_categoria(
        tp_movimentacao=categoria.tp_movimentacao,
        descricao=categoria.descricao
    )
    if "erro" in resultado:
        raise HTTPException(status_code=400, detail=resultado["erro"])
    return resultado

@router.put("/categorias/{id_categoria}")
def atualizar_categoria(id_categoria: int, categoria: CategoriaCreate):
    resultado = categoria_crud.atualizar_categoria(
        id_categoria=id_categoria,
        tp_movimentacao=categoria.tp_movimentacao,
        descricao=categoria.descricao
    )
    if "erro" in resultado:
        raise HTTPException(status_code=400, detail=resultado["erro"])
    return resultado

@router.delete("/categorias/{id_categoria}")
def excluir_categoria(id_categoria: int):
    resultado = categoria_crud.excluir_categoria(id_categoria)
    if "erro" in resultado:
        raise HTTPException(status_code=400, detail=resultado["erro"])
    return resultado