"""
    Arquivo de importação de rotas
"""

# * Importando classes de seus respectivos módulos dentro do pacote atual. Fazemos, por padrão, o import relativo
# * (com ponto inicial) para que o Python saiba que estamos importando de um módulo dentro do mesmo pacote.

from .search_sales_orders import router as search_sales_orders_router

__all__ = [
    "search_sales_orders_router",
]