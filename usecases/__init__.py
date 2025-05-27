from usecases.predict_casas import predict_casa
from usecases.predict_departamentos import predict_departamento
from usecases.get_stats import (
    get_precio_m2_casas, get_precio_m2_departamentos,
    get_stats_casas, get_stats_departamentos,
    get_total_casas, get_total_departamentos, get_total_propiedades
)
from usecases.get_fibra_price import get_fibra_price

__all__ = [
    'predict_casa',
    'predict_departamento',
    'get_precio_m2_casas',
    'get_precio_m2_departamentos',
    'get_stats_casas',
    'get_stats_departamentos',
    'get_total_casas',
    'get_total_departamentos',
    'get_total_propiedades',
    'get_fibra_price'
] 