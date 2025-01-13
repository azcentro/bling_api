from fastapi import APIRouter, HTTPException
from app.config import BLING_CLIENT_ID, BLING_CLIENT_SECRET, BLING_TOKEN_URL, BLING_REFRESH_TOKEN
import base64
import requests
from dotenv import set_key
from pathlib import Path
import logging

router = APIRouter()

def update_env_variable(key: str, value: str, env_file: str = ".env"):
    """
    Atualiza ou adiciona uma variável no arquivo .env.
    
    :param key: Chave da variável de ambiente
    :param value: Valor da variável de ambiente
    :param env_file: Caminho do arquivo .env
    """
    env_path = Path(env_file)
    if not env_path.exists():
        logging.error(f"Arquivo {env_file} não encontrado.")
        raise FileNotFoundError(f"Arquivo {env_file} não encontrado.")
    
    if not env_path.exists():
        logging.info(f"Variável '{key}' atualizada no arquivo {env_file}.")
        raise FileNotFoundError(f"Variável '{key}' atualizada no arquivo {env_file}.")
    
    set_key(env_path, key, value)
    logging.info(f"Variável '{key}' atualizada no arquivo {env_file}.")

@router.post("/auth/refresh_token", tags=["Auth"], summary="Obter Token de Acesso")
def get_token():
    """
    Obtem o token de Acesso do Bling usando o refresh_token.
    """
    try:
        # Codifica as credenciais em Base64
        credentials = f"{BLING_CLIENT_ID}:{BLING_CLIENT_SECRET}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()


        # Configura os dados e cabeçalhos da requisição
        data = {"grant_type": "refresh_token", 
                "refresh_token": BLING_REFRESH_TOKEN}
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {encoded_credentials}",
        }

        # Envia a requisição POST para o endpoint de token
        response = requests.post(BLING_TOKEN_URL, data=data, headers=headers)
        response.raise_for_status()

        update_env_variable("BLING_ACCESS_TOKEN", response.json()["access_token"])
        update_env_variable("BLING_REFRESH_TOKEN", response.json()["refresh_token"])

        # Retorna a resposta JSON
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Erro ao obter token: {e}")
        raise HTTPException(status_code=400, detail=f"Erro ao obter token: {e}")
