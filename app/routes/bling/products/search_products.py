from fastapi import APIRouter, HTTPException, Query
import logging
from app.services.bling_client import BlingClient
from typing import Optional, List

router = APIRouter()

@router.get("/products/search", status_code=200, tags=["Bling"],
    summary="Logs dos Endpoints",
    description="Retorna os logs armazenados no arquivo com filtros opcionais.",)
def search_products(
    nome: Optional[str] = Query(None, description="Descrição para buscar produtos"),
    page: int = Query(1, description="Número da página"),
    limit: int = Query(10, description="Quantidade de produtos por página"),
    idsProdutos: Optional[List[str]] = Query(None, description="IDs dos produtos separados por vírgula")
):
    """
    Rota para buscar produtos com filtros.
    """
    try:
        products = BlingClient.search_products(nome=nome, page=page, limit=limit, idsProdutos=idsProdutos)
        return products
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))