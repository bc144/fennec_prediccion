from typing import List
from domain.models import FibraResponse
from domain.exceptions import ErrorFibras
from infra.data import FibrasRepository

def get_fibra(nombre: str) -> FibraResponse:
    """
    Caso de uso para obtener datos de una fibra específica
    
    Args:
        nombre: Nombre de la fibra
        
    Returns:
        Datos de la fibra incluyendo su variación
        
    Raises:
        ErrorFibras: Si hay un error al obtener los datos
    """
    try:
        repo = FibrasRepository()
        return repo.get_fibra(nombre)
    except Exception as e:
        raise ErrorFibras(str(e))

def get_all_fibras() -> List[FibraResponse]:
    """
    Caso de uso para obtener datos de todas las fibras
    
    Returns:
        Lista con los datos de todas las fibras
        
    Raises:
        ErrorFibras: Si hay un error al obtener los datos
    """
    try:
        repo = FibrasRepository()
        return repo.get_all_fibras()
    except Exception as e:
        raise ErrorFibras(str(e)) 