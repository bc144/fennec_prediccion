from domain.models import (
    PrecioM2Response, 
    EstadisticasPrecios, 
    TotalResponse, 
    PreciosAlcaldiaResponse,
    PrecioM2AlcaldiaResponse
)
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
        return precio_m2
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
        return precio_m2
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
        stats = repo.get_stats_casas()
        return stats
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
        stats = repo.get_stats_departamentos()
        return stats
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
        return total
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
        return total
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
        return total
    except Exception as e:
        raise ErrorEstadisticas(str(e))


def get_precios_por_alcaldia_casas() -> PreciosAlcaldiaResponse:
    """
    Caso de uso para obtener precios promedio por alcaldía para casas
    
    Returns:
        Precios promedio por alcaldía
        
    Raises:
        ErrorEstadisticas: Si hay un error al calcular las estadísticas
    """
    try:
        repo = StatsRepository()
        precios = repo.get_precio_promedio_por_alcaldia_casas()
        return PreciosAlcaldiaResponse(precios=precios)
    except Exception as e:
        raise ErrorEstadisticas(str(e))


def get_precios_por_alcaldia_departamentos() -> PreciosAlcaldiaResponse:
    """
    Caso de uso para obtener precios promedio por alcaldía para departamentos
    
    Returns:
        Precios promedio por alcaldía
        
    Raises:
        ErrorEstadisticas: Si hay un error al calcular las estadísticas
    """
    try:
        repo = StatsRepository()
        precios = repo.get_precio_promedio_por_alcaldia_departamentos()
        return PreciosAlcaldiaResponse(precios=precios)
    except Exception as e:
        raise ErrorEstadisticas(str(e))


def get_precios_por_alcaldia_total() -> PreciosAlcaldiaResponse:
    """
    Caso de uso para obtener precios promedio por alcaldía para todas las propiedades
    
    Returns:
        Precios promedio por alcaldía
        
    Raises:
        ErrorEstadisticas: Si hay un error al calcular las estadísticas
    """
    try:
        repo = StatsRepository()
        precios = repo.get_precio_promedio_por_alcaldia_total()
        return PreciosAlcaldiaResponse(precios=precios)
    except Exception as e:
        raise ErrorEstadisticas(str(e))


def get_precio_m2_por_alcaldia_casas() -> PrecioM2AlcaldiaResponse:
    """
    Caso de uso para obtener precio promedio por metro cuadrado por alcaldía para casas
    
    Returns:
        Precios promedio por metro cuadrado por alcaldía
        
    Raises:
        ErrorEstadisticas: Si hay un error al calcular las estadísticas
    """
    try:
        repo = StatsRepository()
        precios = repo.get_precio_m2_por_alcaldia_casas()
        return PrecioM2AlcaldiaResponse(precios=precios)
    except Exception as e:
        raise ErrorEstadisticas(str(e))


def get_precio_m2_por_alcaldia_departamentos() -> PrecioM2AlcaldiaResponse:
    """
    Caso de uso para obtener precio promedio por metro cuadrado por alcaldía para departamentos
    
    Returns:
        Precios promedio por metro cuadrado por alcaldía
        
    Raises:
        ErrorEstadisticas: Si hay un error al calcular las estadísticas
    """
    try:
        repo = StatsRepository()
        precios = repo.get_precio_m2_por_alcaldia_departamentos()
        return PrecioM2AlcaldiaResponse(precios=precios)
    except Exception as e:
        raise ErrorEstadisticas(str(e))


def get_precio_m2_por_alcaldia_total() -> PrecioM2AlcaldiaResponse:
    """
    Caso de uso para obtener precio promedio por metro cuadrado por alcaldía para todas las propiedades
    
    Returns:
        Precios promedio por metro cuadrado por alcaldía
        
    Raises:
        ErrorEstadisticas: Si hay un error al calcular las estadísticas
    """
    try:
        repo = StatsRepository()
        precios = repo.get_precio_m2_por_alcaldia_total()
        return PrecioM2AlcaldiaResponse(precios=precios)
    except Exception as e:
        raise ErrorEstadisticas(str(e)) 