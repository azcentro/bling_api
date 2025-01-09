from fastapi import APIRouter, HTTPException
from app.config import BLING_CLIENT_ID, BLING_CLIENT_SECRET, BLING_TOKEN_URL
import base64
import requests

router = APIRouter()

@router.post("/auth/token", tags=["Auth"], summary="Obter Token OAuth")
def get_token(code: str):
    """
    Obtem o token OAuth do Bling usando o código de autorização.
    """
    try:
        # Codifica as credenciais em Base64
        credentials = f"{BLING_CLIENT_ID}:{BLING_CLIENT_SECRET}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()

        # Configura os dados e cabeçalhos da requisição
        data = {"grant_type": "authorization_code", "code": code}
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {encoded_credentials}",
        }

        # Envia a requisição POST para o endpoint de token
        response = requests.post(BLING_TOKEN_URL, data=data, headers=headers)
        response.raise_for_status()

        # Retorna a resposta JSON
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Erro ao obter token: {e}")
