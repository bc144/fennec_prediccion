from domain.models import FibraPrecio
from domain.exceptions import ErrorFibras
from infra.services.fibra_prices import FibraPriceService


def get_fibra_price(fibra_name: str) -> FibraPrecio:
    """
    Obtiene el precio más reciente de una FIBRA
    
    Args:
        fibra_name: Nombre de la FIBRA (ej: 'funo')
        
    Returns:
        Datos de la FIBRA incluyendo precio y variación
        
    Raises:
        ErrorFibras: Si no se encuentra la FIBRA o hay error
    """
    try:
        service = FibraPriceService()
        return service.get_price(fibra_name)
    except Exception as e:
        raise ErrorFibras(str(e)) 