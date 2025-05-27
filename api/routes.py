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
    get_precio_m2_por_alcaldia_casas,
    get_precio_m2_por_alcaldia_departamentos,
    get_precio_m2_por_alcaldia_total
)

router = APIRouter(prefix="/stats")


@router.get("/casas/precio-m2", response_model=PrecioM2Response)
def precio_m2_casas():
    try:
        return get_precio_m2_casas()
    except ErrorEstadisticas as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/departamentos/precio-m2", response_model=PrecioM2Response)
def precio_m2_departamentos():
    try:
        return get_precio_m2_departamentos()
    except ErrorEstadisticas as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/casas/stats", response_model=EstadisticasPrecios)
def stats_casas():
    try:
        return get_stats_casas()
    except ErrorEstadisticas as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/departamentos/stats", response_model=EstadisticasPrecios)
def stats_departamentos():
    try:
        return get_stats_departamentos()
    except ErrorEstadisticas as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/casas/total", response_model=TotalResponse)
def total_casas():
    try:
        return get_total_casas()
    except ErrorEstadisticas as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/departamentos/total", response_model=TotalResponse)
def total_departamentos():
    try:
        return get_total_departamentos()
    except ErrorEstadisticas as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/total", response_model=TotalResponse)
def total_propiedades():
    try:
        return get_total_propiedades()
    except ErrorEstadisticas as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/casas/precios-por-alcaldia", response_model=PreciosAlcaldiaResponse)
def precios_por_alcaldia_casas():
    try:
        return get_precios_por_alcaldia_casas()
    except ErrorEstadisticas as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/departamentos/precios-por-alcaldia", response_model=PreciosAlcaldiaResponse)
def precios_por_alcaldia_departamentos():
    try:
        return get_precios_por_alcaldia_departamentos()
    except ErrorEstadisticas as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/casas/precio-m2-por-alcaldia", response_model=PrecioM2AlcaldiaResponse)
def precio_m2_por_alcaldia_casas():
    try:
        return get_precio_m2_por_alcaldia_casas()
    except ErrorEstadisticas as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/departamentos/precio-m2-por-alcaldia", response_model=PrecioM2AlcaldiaResponse)
def precio_m2_por_alcaldia_departamentos():
    try:
        return get_precio_m2_por_alcaldia_departamentos()
    except ErrorEstadisticas as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/precio-m2-por-alcaldia", response_model=PrecioM2AlcaldiaResponse)
def precio_m2_por_alcaldia_total():
    try:
        return get_precio_m2_por_alcaldia_total()
    except ErrorEstadisticas as e:
        raise HTTPException(status_code=500, detail=str(e)) 