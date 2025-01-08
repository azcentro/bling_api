import os
from dotenv import load_dotenv
import pytz
import logging

load_dotenv()

# Configurações de Banco e API
BLING_CLIENT_ID = os.getenv("BLING_CLIENT_ID")
BLING_CLIENT_SECRET = os.getenv("BLING_CLIENT_SECRET")
BLING_ACCESS_TOKEN = os.getenv("BLING_ACCESS_TOKEN")
BLING_BASE_URL = os.getenv("BLING_BASE_URL")
BLING_TOKEN_URL = os.getenv("BLING_TOKEN_URL")
BLING_REFRESH_TOKEN = os.getenv("BLING_REFRESH_TOKEN")

# Verificação de variáveis de ambiente obrigatórias
if not all([BLING_ACCESS_TOKEN, BLING_CLIENT_ID, BLING_CLIENT_SECRET]):
    raise ValueError("Variáveis de ambiente não configuradas corretamente.")
