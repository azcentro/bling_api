import requests
import logging
from app.config import BLING_BASE_URL, BLING_ACCESS_TOKEN

class BlingClient:
    # Outras configurações e métodos...

    def _get_headers():
        return {"Authorization": f"Bearer {BLING_ACCESS_TOKEN}"}

    @classmethod
    def search_products(cls, description=None, page=1, limit=10):
        """
        Busca produtos na API do Bling com base em descrição e paginação.
        """
        url = f"{BLING_BASE_URL}produtos"
        headers = cls._get_headers()
        params = {
            "descricao": description,
            "page": page,
            "limit": limit
        }
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
