from fastapi import APIRouter, HTTPException, status
from domain.models import CasaInputData, Prediccion
from domain.exceptions import AlcaldiaNoEncontrada, ModeloNoDisponible, ErrorPrediccion
from usecases.predict_casas import predict_casa

# Crear el router
router = APIRouter(
    prefix="/casas",
    tags=["casas"],
    responses={
        404: {"description": "No encontrado"},
        500: {"description": "Error interno del servidor"}
    }
)


@router.post("/predict", response_model=Prediccion, status_code=status.HTTP_200_OK)
async def predecir_casa(input_data: CasaInputData):
    """
    Predice el precio de una casa en la Ciudad de México.
    
    Args:
        input_data: Características de la casa (alcaldía, metros cuadrados, recámaras, baños, estacionamientos)
        
    Returns:
        Predicción con el precio estimado y metadatos
    
    Raises:
        HTTPException: Si hay un error en la predicción
    """
    try:
        result = predict_casa(input_data)
        return result
    
    except AlcaldiaNoEncontrada as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Alcaldía no encontrada: {str(e)}"
        )
    
    except ModeloNoDisponible as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al cargar el modelo: {str(e)}"
        )
    
    except ErrorPrediccion as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error en la predicción: {str(e)}"
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error inesperado: {str(e)}"
        ) 