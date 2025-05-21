from fastapi import APIRouter, HTTPException, status
from domain.models import DepartamentoInputData, Prediccion
from domain.exceptions import AlcaldiaNoEncontrada, ModeloNoDisponible, ErrorPrediccion
from usecases.predict_departamentos import predict_departamento

# Crear el router
router = APIRouter(
    prefix="/departamentos",
    tags=["departamentos"],
    responses={
        404: {"description": "No encontrado"},
        500: {"description": "Error interno del servidor"}
    }
)


@router.post("/predict", response_model=Prediccion, status_code=status.HTTP_200_OK)
async def predecir_departamento(input_data: DepartamentoInputData):
    """
    Predice el precio de un departamento en la Ciudad de México.
    
    Args:
        input_data: Características del departamento (alcaldía, metros cuadrados, recámaras, baños, estacionamientos)
        
    Returns:
        Predicción con el precio estimado y metadatos
    
    Raises:
        HTTPException: Si hay un error en la predicción
    """
    try:
        result = predict_departamento(input_data)
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