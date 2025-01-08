import requests
from fastapi import APIRouter, HTTPException, Query
import logging
from app.config import BLING_TOKEN_URL, BLING_CLIENT_ID, BLING_CLIENT_SECRET, BLING_REFRESH_TOKEN

router = APIRouter()

def refresh_access_token():
    try:
        payload = {
            "grant_type": "refresh_token",
            "refresh_token": BLING_REFRESH_TOKEN,
            "client_id": BLING_CLIENT_ID,
            "client_secret": BLING_CLIENT_SECRET
        }
        response = requests.post(BLING_TOKEN_URL, data=payload)
        response.raise_for_status()
        
        # Parse response
        token_data = response.json()
        access_token = token_data.get("access_token")
        new_refresh_token = token_data.get("refresh_token")
        
        if access_token:
            print("Novo token de acesso:", access_token)
            if new_refresh_token:
                print("Novo refresh token:", new_refresh_token)
            return token_data
        else:
            print("Erro: Não foi possível obter o token.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Erro ao obter o token: {e}")
        return None
