from fastapi import FastAPI

# Importação de rotas
from app.routes.logs import *
from app.routes.bling.products import *
from app.routes.bling.sales_orders import *
from app.routes.bling_config import *

app = FastAPI(title="Integração com Bling API", version="3.0.0")

# Incluindo rotas
app.include_router(logs_router)

app.include_router(search_products_router)
app.include_router(search_sales_orders_router)

app.include_router(refresh_access_token_router)
app.include_router(auth_token_router)