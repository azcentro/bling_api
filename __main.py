from fastapi import FastAPI

# Importação de rotas
from app.routes.logs import *
from app.routes.bling import *

app = FastAPI(title="Chatbot WhatsApp Scheduler")

# Incluindo rotas
app.include_router(logs_router)

app.include_router(search_products_router)

