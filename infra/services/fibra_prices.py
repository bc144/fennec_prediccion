import yfinance as yf
from datetime import datetime
from typing import Optional, Tuple
from domain.exceptions import DomainException


class FibraNoEncontrada(DomainException):
    """Se lanza cuando no se encuentra información para una FIBRA"""
    pass


class FibraPriceService:
    """Servicio para consultar precios de FIBRAs"""
    
    def __init__(self):
        # Mapeo de nombres cortos a tickers completos
        self.ticker_map = {
            'funo': 'FUNO11.MX',
            'fmty': 'FMTY14.MX',
            'danhos': 'DANHOS13.MX'
        }
    
    def get_latest_price(self, fibra_name: str) -> Tuple[float, datetime]:
        """
        Obtiene el precio más reciente de una FIBRA
        
        Args:
            fibra_name: Nombre corto de la FIBRA (ej: 'funo')
            
        Returns:
            Tupla con (precio, fecha)
            
        Raises:
            FibraNoEncontrada: Si no se encuentra la FIBRA o no hay datos
        """
        try:
            # Obtener el ticker completo
            ticker = self.ticker_map.get(fibra_name.lower())
            if not ticker:
                raise FibraNoEncontrada(f"FIBRA no soportada: {fibra_name}")
            
            # Obtener datos de yfinance
            fibra = yf.Ticker(ticker)
            hist = fibra.history(period="1d")
            
            if hist.empty:
                raise FibraNoEncontrada(f"No hay datos para la FIBRA: {fibra_name}")
            
            # Obtener el último precio de cierre y su fecha
            last_row = hist.iloc[-1]
            precio = last_row['Close']
            fecha = hist.index[-1].to_pydatetime()
            
            return precio, fecha
            
        except Exception as e:
            if isinstance(e, FibraNoEncontrada):
                raise
            raise FibraNoEncontrada(f"Error al consultar FIBRA {fibra_name}: {str(e)}") 