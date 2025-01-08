from fastapi import FastAPI

# Importação de rotas
from app.routes.logs import *
from app.routes.bling import *

app = FastAPI(title="Integração com Bling API", version="3.0.0")

# Incluindo rotas
app.include_router(logs_router)

app.include_router(search_products_router)

