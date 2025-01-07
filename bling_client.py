import os
import requests
from dotenv import load_dotenv

load_dotenv()

class BlingClient:
    TOKEN_URL = os.getenv("BLING_TOKEN_URL")
    BASE_URL = os.getenv("BLING_BASE_URL")
    CLIENT_ID = os.getenv("BLING_CLIENT_ID")
    CLIENT_SECRET = os.getenv("BLING_CLIENT_SECRET")
    _access_token = None

    @classmethod
    def _get_access_token(cls):
        """Obtém o token de acesso OAuth 2.0."""
        if cls._access_token is None:
            response = requests.post(
                cls.TOKEN_URL,
                data={
                    "grant_type": "client_credentials",
                    "client_id": cls.CLIENT_ID,
                    "client_secret": cls.CLIENT_SECRET
                }
            )
            response.raise_for_status()
            cls._access_token = response.json().get("access_token")
        return cls._access_token

    @classmethod
    def _get_headers(cls):
        """Headers com o token de acesso."""
        return {"Authorization": f"Bearer {cls._get_access_token()}"}

    @classmethod
    def list_products(cls):
        """Lista todos os produtos cadastrados."""
        url = f"{cls.BASE_URL}produtos"
        response = requests.get(url, headers=cls._get_headers())
        response.raise_for_status()
        return response.json()

    @classmethod
    def get_product(cls, product_id):
        """Obtém informações de um produto específico pelo ID."""
        url = f"{cls.BASE_URL}produtos/{product_id}"
        response = requests.get(url, headers=cls._get_headers())
        response.raise_for_status()
        return response.json()
