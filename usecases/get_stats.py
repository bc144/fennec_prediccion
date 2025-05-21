from domain.models import PrecioM2Response, EstadisticasPrecios, TotalResponse
from domain.exceptions import ErrorEstadisticas
from infra.data.stats_repo import StatsRepository


def get_precio_m2_casas() -> PrecioM2Response:
    """
    Caso de uso para obtener el precio promedio por metro cuadrado de casas
    
    Returns:
        Precio promedio por metro cuadrado de casas
        
    Raises:
        ErrorEstadisticas: Si hay un error al calcular las estadísticas
    """
    try:
        repo = StatsRepository()
        precio_m2 = repo.get_precio_m2_casas()
        return PrecioM2Response(precio_m2=precio_m2)
    except Exception as e:
        raise ErrorEstadisticas(str(e))


def get_precio_m2_departamentos() -> PrecioM2Response:
    """
    Caso de uso para obtener el precio promedio por metro cuadrado de departamentos
    
    Returns:
        Precio promedio por metro cuadrado de departamentos
        
    Raises:
        ErrorEstadisticas: Si hay un error al calcular las estadísticas
    """
    try:
        repo = StatsRepository()
        precio_m2 = repo.get_precio_m2_departamentos()
        return PrecioM2Response(precio_m2=precio_m2)
    except Exception as e:
        raise ErrorEstadisticas(str(e))


def get_stats_casas() -> EstadisticasPrecios:
    """
    Caso de uso para obtener estadísticas de precios de casas
    
    Returns:
        Estadísticas detalladas de precios de casas
        
    Raises:
        ErrorEstadisticas: Si hay un error al calcular las estadísticas
    """
    try:
        repo = StatsRepository()
        datos = repo.get_stats_casas()
        return EstadisticasPrecios(**datos)
    except Exception as e:
        raise ErrorEstadisticas(str(e))


def get_stats_departamentos() -> EstadisticasPrecios:
    """
    Caso de uso para obtener estadísticas de precios de departamentos
    
    Returns:
        Estadísticas detalladas de precios de departamentos
        
    Raises:
        ErrorEstadisticas: Si hay un error al calcular las estadísticas
    """
    try:
        repo = StatsRepository()
        datos = repo.get_stats_departamentos()
        return EstadisticasPrecios(**datos)
    except Exception as e:
        raise ErrorEstadisticas(str(e))


def get_total_casas() -> TotalResponse:
    """
    Caso de uso para obtener el total de casas
    
    Returns:
        Total de casas
        
    Raises:
        ErrorEstadisticas: Si hay un error al calcular las estadísticas
    """
    try:
        repo = StatsRepository()
        total = repo.get_total_casas()
        return TotalResponse(total=total)
    except Exception as e:
        raise ErrorEstadisticas(str(e))


def get_total_departamentos() -> TotalResponse:
    """
    Caso de uso para obtener el total de departamentos
    
    Returns:
        Total de departamentos
        
    Raises:
        ErrorEstadisticas: Si hay un error al calcular las estadísticas
    """
    try:
        repo = StatsRepository()
        total = repo.get_total_departamentos()
        return TotalResponse(total=total)
    except Exception as e:
        raise ErrorEstadisticas(str(e))


def get_total_propiedades() -> TotalResponse:
    """
    Caso de uso para obtener el total de propiedades
    
    Returns:
        Total de propiedades
        
    Raises:
        ErrorEstadisticas: Si hay un error al calcular las estadísticas
    """
    try:
        repo = StatsRepository()
        total = repo.get_total_propiedades()
        return TotalResponse(total=total)
    except Exception as e:
        raise ErrorEstadisticas(str(e)) 