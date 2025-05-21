from pydantic import BaseModel, Field
from typing import Optional, Dict, List


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