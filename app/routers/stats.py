from fastapi import APIRouter, HTTPException
from domain.models import (
    PrecioM2Response, 
    EstadisticasPrecios, 
    TotalResponse, 
    PreciosAlcaldiaResponse,
    PrecioM2AlcaldiaResponse
)
from domain.exceptions import ErrorEstadisticas
from usecases.get_stats import (
    get_precio_m2_casas,
    get_precio_m2_departamentos,
    get_stats_casas,
    get_stats_departamentos,
    get_total_casas,
    get_total_departamentos,
    get_total_propiedades,
    get_precios_por_alcaldia_casas,
    get_precios_por_alcaldia_departamentos,
    get_precios_por_alcaldia_total,
    get_precio_m2_por_alcaldia_casas,
    get_precio_m2_por_alcaldia_departamentos,
    get_precio_m2_por_alcaldia_total
)

router = APIRouter(prefix="/stats", tags=["Estadísticas"])


@router.get("/casas/precio-m2", response_model=PrecioM2Response)
def precio_m2_casas():
    """Obtiene el precio promedio por metro cuadrado de casas"""
    try:
        return get_precio_m2_casas()
    except ErrorEstadisticas as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/departamentos/precio-m2", response_model=PrecioM2Response)
def precio_m2_departamentos():
    """Obtiene el precio promedio por metro cuadrado de departamentos"""
    try:
        return get_precio_m2_departamentos()
    except ErrorEstadisticas as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/casas/stats", response_model=EstadisticasPrecios)
def stats_casas():
    """Obtiene estadísticas detalladas de precios de casas"""
    try:
        return get_stats_casas()
    except ErrorEstadisticas as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/departamentos/stats", response_model=EstadisticasPrecios)
def stats_departamentos():
    """Obtiene estadísticas detalladas de precios de departamentos"""
    try:
        return get_stats_departamentos()
    except ErrorEstadisticas as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/casas/total", response_model=TotalResponse)
def total_casas():
    """Obtiene el total de casas"""
    try:
        return get_total_casas()
    except ErrorEstadisticas as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/departamentos/total", response_model=TotalResponse)
def total_departamentos():
    """Obtiene el total de departamentos"""
    try:
        return get_total_departamentos()
    except ErrorEstadisticas as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/total", response_model=TotalResponse)
def total_propiedades():
    """Obtiene el total de todas las propiedades"""
    try:
        return get_total_propiedades()
    except ErrorEstadisticas as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/casas/precios-por-alcaldia", response_model=PreciosAlcaldiaResponse)
def precios_por_alcaldia_casas():
    """Obtiene los precios promedio por alcaldía para casas"""
    try:
        return get_precios_por_alcaldia_casas()
    except ErrorEstadisticas as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/departamentos/precios-por-alcaldia", response_model=PreciosAlcaldiaResponse)
def precios_por_alcaldia_departamentos():
    """Obtiene los precios promedio por alcaldía para departamentos"""
    try:
        return get_precios_por_alcaldia_departamentos()
    except ErrorEstadisticas as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/precios-por-alcaldia", response_model=PreciosAlcaldiaResponse)
def precios_por_alcaldia_total():
    """Obtiene los precios promedio por alcaldía para todas las propiedades"""
    try:
        return get_precios_por_alcaldia_total()
    except ErrorEstadisticas as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/casas/precio-m2-por-alcaldia", response_model=PrecioM2AlcaldiaResponse)
def precio_m2_por_alcaldia_casas():
    """Obtiene los precios promedio por metro cuadrado por alcaldía para casas"""
    try:
        return get_precio_m2_por_alcaldia_casas()
    except ErrorEstadisticas as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/departamentos/precio-m2-por-alcaldia", response_model=PrecioM2AlcaldiaResponse)
def precio_m2_por_alcaldia_departamentos():
    """Obtiene los precios promedio por metro cuadrado por alcaldía para departamentos"""
    try:
        return get_precio_m2_por_alcaldia_departamentos()
    except ErrorEstadisticas as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/precio-m2-por-alcaldia", response_model=PrecioM2AlcaldiaResponse)
def precio_m2_por_alcaldia_total():
    """Obtiene los precios promedio por metro cuadrado por alcaldía para todas las propiedades"""
    try:
        return get_precio_m2_por_alcaldia_total()
    except ErrorEstadisticas as e:
        raise HTTPException(status_code=500, detail=str(e)) 