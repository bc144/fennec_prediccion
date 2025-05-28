from fastapi import APIRouter, HTTPException, status
from typing import List
from domain.models import FibraResponse
from domain.exceptions import ErrorFibras
from usecases.get_fibras import get_fibra, get_all_fibras

# Crear el router
router = APIRouter(
    prefix="/fibras",
    tags=["Fibras"],
    responses={
        404: {"description": "FIBRA no encontrada"},
        500: {"description": "Error interno del servidor"}
    }
)

@router.get("/{nombre}", response_model=FibraResponse)
async def obtener_fibra(nombre: str):
    """
    Obtiene los datos más recientes de una FIBRA específica
    
    Args:
        nombre: Nombre de la FIBRA (ej: FUNO, FMTY, FIBRAPL)
        
    Returns:
        Datos de la FIBRA incluyendo precio, variación y fecha
    """
    try:
        # Limpiar el nombre de la FIBRA de caracteres especiales
        nombre = nombre.strip().upper()
        return get_fibra(nombre)
    except ErrorFibras as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno: {str(e)}"
        )

@router.get("/", response_model=List[FibraResponse])
async def obtener_todas_fibras():
    """
    Obtiene los datos más recientes de todas las FIBRAs disponibles
    
    Returns:
        Lista con los datos de todas las FIBRAs
    """
    try:
        return get_all_fibras()
    except ErrorFibras as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error interno: {str(e)}"
        ) 