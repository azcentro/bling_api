from fastapi import APIRouter, HTTPException, Query
import logging
from app.services.bling_client import BlingClient
from typing import Optional, List
import requests

router = APIRouter()

@router.get("/sales_orders/search", status_code=200, tags=["Bling"],
    summary="Busca por Pedidos de Venda",
    description="Retorna pedidos de venda com base nos filtros fornecidos.")
def search_sales_orders(
    pagina: int = Query(1, description="Número da página"),
    limite: int = Query(10, description="Quantidade de itens por página"),
    idContato: Optional[int] = Query(None, description="ID do contato"),
    idsSituacoes: Optional[List[int]] = Query(None, description="IDs das situações separados por vírgula"),
    dataInicial: Optional[str] = Query(None, description="Data inicial no formato yyyy-mm-dd"),
    dataFinal: Optional[str] = Query(None, description="Data final no formato yyyy-mm-dd"),
    dataAlteracaoInicial: Optional[str] = Query(None, description="Data inicial de alteração no formato yyyy-mm-dd"),
    dataAlteracaoFinal: Optional[str] = Query(None, description="Data final de alteração no formato yyyy-mm-dd"),
    dataPrevistaInicial: Optional[str] = Query(None, description="Data inicial prevista no formato yyyy-mm-dd"),
    dataPrevistaFinal: Optional[str] = Query(None, description="Data final prevista no formato yyyy-mm-dd"),
    numero: Optional[int] = Query(None, description="Número do pedido"),
    idLoja: Optional[int] = Query(None, description="ID da loja"),
    idVendedor: Optional[int] = Query(None, description="ID do vendedor"),
    idControleCaixa: Optional[int] = Query(None, description="ID do controle de caixa"),
    numerosLojas: Optional[List[str]] = Query(None, description="Números de lojas separados por vírgula"),
):
    """
    Rota para buscar pedidos de venda com base nos filtros fornecidos.
    """
    try:
        sales_orders = BlingClient.search_sales_orders(
            pagina=pagina,
            limite=limite,
            idContato=idContato,
            idsSituacoes=idsSituacoes,
            dataInicial=dataInicial,
            dataFinal=dataFinal,
            dataAlteracaoInicial=dataAlteracaoInicial,
            dataAlteracaoFinal=dataAlteracaoFinal,
            dataPrevistaInicial=dataPrevistaInicial,
            dataPrevistaFinal=dataPrevistaFinal,
            numero=numero,
            idLoja=idLoja,
            idVendedor=idVendedor,
            idControleCaixa=idControleCaixa,
            numerosLojas=numerosLojas,
        )
        return sales_orders
    except requests.HTTPError as e:
        logging.error(f"Erro ao buscar pedidos de venda: {e}")
        raise HTTPException(status_code=e.response.status_code, detail=e.response.text)
    except Exception as e:
        logging.error(f"Erro inesperado: {e}")
        raise HTTPException(status_code=500, detail="Erro interno no servidor")
