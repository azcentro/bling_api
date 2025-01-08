"""
    Arquivo de importação de rotas
"""

# * Importando classes de seus respectivos módulos dentro do pacote atual. Fazemos, por padrão, o import relativo
# * (com ponto inicial) para que o Python saiba que estamos importando de um módulo dentro do mesmo pacote.

from .refresh_access_token import router as refresh_access_token_router

__all__ = [
    "refresh_access_token_router",
]