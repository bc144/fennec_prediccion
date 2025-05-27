from app.routers.casas import router as casas_router
from app.routers.departamentos import router as departamentos_router
from app.routers.stats import router as stats_router
from app.routers.fibras import router as fibras_router

__all__ = [
    'casas_router',
    'departamentos_router',
    'stats_router',
    'fibras_router'
] 