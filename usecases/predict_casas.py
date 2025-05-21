import datetime
from typing import Dict, Any

from domain.models import Prediccion, CasaInputData
from domain.exceptions import AlcaldiaNoEncontrada, ModeloNoDisponible, ErrorPrediccion

from infra.data.casas_repo import CasasRepository


def predict_casa(input_data: CasaInputData) -> Prediccion:
    """
    Caso de uso para predecir el precio de una casa
    
    Args:
        input_data: Datos de entrada para la predicción
        
    Returns:
        Predicción con el precio estimado
    
    Raises:
        AlcaldiaNoEncontrada: Si no se encuentra información para la alcaldía
        ModeloNoDisponible: Si no se puede cargar el modelo
        ErrorPrediccion: Si hay un error en el proceso de predicción
    """
    try:
        # 1. Preparar datos para el modelo
        model_input = {
            'alcaldia': input_data.alcaldia,
            'metros_cuadrados': input_data.metros_cuadrados,
            'recamaras': input_data.recamaras,
            'banos': input_data.banos,
            'estacionamientos': input_data.estacionamientos
        }
        
        # 2. Cargar repositorio y hacer predicción
        repo = CasasRepository()
        precio_estimado = repo.predict(model_input)
        
        # 3. Construir y retornar la respuesta
        return Prediccion(
            tipo_propiedad="casa",
            precio_estimado=precio_estimado,
            alcaldia=input_data.alcaldia,
            caracteristicas={
                'metros_cuadrados': input_data.metros_cuadrados,
                'recamaras': input_data.recamaras,
                'banos': input_data.banos,
                'estacionamientos': input_data.estacionamientos
            },
            fecha_prediccion=datetime.datetime.now().isoformat()
        )
    
    except (AlcaldiaNoEncontrada, ModeloNoDisponible):
        # Dejar que estas excepciones se propaguen tal cual
        raise
    except Exception as e:
        # Otras excepciones se convierten en ErrorPrediccion
        raise ErrorPrediccion(str(e)) 