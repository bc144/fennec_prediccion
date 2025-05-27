from domain.models import FibraPrecio
from infra.services.fibra_prices import FibraPriceService, FibraNoEncontrada


def get_fibra_price(fibra_name: str) -> FibraPrecio:
    """
    Caso de uso para obtener el precio actual de una FIBRA
    
    Args:
        fibra_name: Nombre corto de la FIBRA (ej: 'funo')
        
    Returns:
        Objeto FibraPrecio con la información
        
    Raises:
        FibraNoEncontrada: Si no se encuentra la FIBRA o no hay datos
    """
    try:
        service = FibraPriceService()
        precio, fecha = service.get_latest_price(fibra_name)
        
        return FibraPrecio(
            ticker=fibra_name.upper(),
            precio=precio,
            fecha=fecha
        )
    except Exception as e:
        if isinstance(e, FibraNoEncontrada):
            raise
        raise FibraNoEncontrada(str(e)) 