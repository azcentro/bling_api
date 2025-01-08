import requests
import logging
from app.config import BLING_BASE_URL, BLING_ACCESS_TOKEN
from typing import Optional, List

class BlingClient:
    @classmethod
    def search_products(cls, nome=None, page=1, limit=10, idsProdutos=None):
        """
        Busca produtos na API do Bling com base no nome e paginação.
        """
        url = f"{BLING_BASE_URL}/produtos"
        headers = {"Authorization": f"Bearer {BLING_ACCESS_TOKEN}"}
        params = {
            "nome": nome,
            "page": page,
            "limit": limit,
            "idsProdutos[]": idsProdutos
        }
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    @classmethod
    def search_sales_orders(
        cls,
        pagina: int = 1,
        limite: int = 10,
        idContato: Optional[int] = None,
        idsSituacoes: Optional[List[int]] = None,
        dataInicial: Optional[str] = None,
        dataFinal: Optional[str] = None,
        dataAlteracaoInicial: Optional[str] = None,
        dataAlteracaoFinal: Optional[str] = None,
        dataPrevistaInicial: Optional[str] = None,
        dataPrevistaFinal: Optional[str] = None,
        numero: Optional[int] = None,
        idLoja: Optional[int] = None,
        idVendedor: Optional[int] = None,
        idControleCaixa: Optional[int] = None,
        numerosLojas: Optional[List[str]] = None,
    ):
        
        url = f"{BLING_BASE_URL}/pedidos/vendas"
        headers = {"Authorization": f"Bearer {BLING_ACCESS_TOKEN}"}
        
        params = {
            "pagina": pagina,
            "limite": limite,
            "idContato": idContato,
            "idsSituacoes[]": idsSituacoes,
            "dataInicial": dataInicial,
            "dataFinal": dataFinal,
            "dataAlteracaoInicial": dataAlteracaoInicial,
            "dataAlteracaoFinal": dataAlteracaoFinal,
            "dataPrevistaInicial": dataPrevistaInicial,
            "dataPrevistaFinal": dataPrevistaFinal,
            "numero": numero,
            "idLoja": idLoja,
            "idVendedor": idVendedor,
            "idControleCaixa": idControleCaixa,
            "numerosLojas[]": numerosLojas,
        }
        response = requests.get(url, headers=headers, params={k: v for k, v in params.items() if v is not None})
        response.raise_for_status()
        return response.json()

