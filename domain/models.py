from pydantic import BaseModel, Field
from typing import Optional, Dict, List
from datetime import datetime


class CasaInputData(BaseModel):
    """Modelo para los datos de entrada de una casa"""
    alcaldia: str
    metros_cuadrados: float = Field(..., gt=0)
    recamaras: int = Field(..., ge=0)
    banos: int = Field(..., ge=0)
    estacionamientos: int = Field(..., ge=0)


class DepartamentoInputData(BaseModel):
    """Modelo para los datos de entrada de un departamento"""
    alcaldia: str
    metros_cuadrados: float = Field(..., gt=0)
    recamaras: int = Field(..., ge=0)
    banos: int = Field(..., ge=0)
    estacionamientos: int = Field(..., ge=0)


class Prediccion(BaseModel):
    """Modelo con la predicción de precio de propiedad"""
    tipo_propiedad: str
    precio_estimado: float
    alcaldia: str
    caracteristicas: Dict[str, float]
    fecha_prediccion: str


class PrecioM2Response(BaseModel):
    """Respuesta con precio promedio por metro cuadrado"""
    precio_m2: float


class EstadisticasPrecios(BaseModel):
    """Estadísticas de precios para un tipo de propiedad"""
    precio_minimo: float
    precio_maximo: float
    precio_promedio: float
    precio_mediana: float


class TotalResponse(BaseModel):
    """Respuesta con total de propiedades"""
    total: int


class FibraPrecio(BaseModel):
    """Modelo para el precio de una FIBRA"""
    ticker: str
    precio: float
    fecha: datetime


class PreciosAlcaldiaResponse(BaseModel):
    """Respuesta con precios promedio por alcaldía"""
    precios: Dict[str, float]


class PrecioM2AlcaldiaResponse(BaseModel):
    """Respuesta con precio promedio por metro cuadrado por alcaldía"""
    precios: Dict[str, float] 