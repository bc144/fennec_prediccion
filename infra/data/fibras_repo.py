import yfinance as yf
import pandas as pd
from typing import List, Dict
from domain.models import FibraResponse
from domain.exceptions import ErrorFibras
from datetime import datetime, timedelta

class FibrasRepository:
    """Repositorio para datos de fibras"""
    
    def __init__(self):
        """Inicializa el repositorio con los tickers de las FIBRAs"""
        # Mapeo de nombres a tickers
        self.fibras: Dict[str, str] = {
            'FUNO': 'FUNO11.MX',
            'FMTY': 'FMTY14.MX',
            'FIBRAPL': 'FIBRAPL14.MX'
        }
    
    def get_fibra(self, nombre: str) -> FibraResponse:
        """
        Obtiene los datos más recientes de una FIBRA específica
        
        Args:
            nombre: Nombre de la FIBRA (ej: FUNO, FMTY)
            
        Returns:
            Datos de la FIBRA con su variación
            
        Raises:
            ErrorFibras: Si no se encuentra la FIBRA o hay error
        """
        try:
            # Buscar el ticker correspondiente
            nombre = nombre.strip().upper()
            if nombre not in self.fibras:
                raise ErrorFibras(f"FIBRA no encontrada: {nombre}")
            
            ticker = self.fibras[nombre]
            
            # Obtener datos de yfinance
            fibra = yf.Ticker(ticker)
            hist = fibra.history(period="2d")
            
            if len(hist) == 0:
                raise ErrorFibras(f"No hay datos disponibles para {nombre}")
            
            # Obtener el último precio
            ultimo_precio = hist['Close'].iloc[-1]
            
            # Calcular la variación si hay más de un precio
            if len(hist) > 1:
                precio_anterior = hist['Close'].iloc[-2]
                variacion = ((ultimo_precio - precio_anterior) / precio_anterior) * 100
            else:
                variacion = 0.0
            
            return FibraResponse(
                nombre=nombre,
                precio=round(float(ultimo_precio), 2),
                variacion=round(float(variacion), 2),
                fecha=hist.index[-1].strftime('%Y-%m-%d')
            )
            
        except ErrorFibras:
            raise
        except Exception as e:
            raise ErrorFibras(f"Error al obtener datos de {nombre}: {str(e)}")
    
    def get_all_fibras(self) -> List[FibraResponse]:
        """
        Obtiene los datos más recientes de todas las FIBRAs
        
        Returns:
            Lista con los datos de todas las FIBRAs
            
        Raises:
            ErrorFibras: Si hay error al obtener los datos
        """
        try:
            return [self.get_fibra(nombre) for nombre in self.fibras.keys()]
        except Exception as e:
            raise ErrorFibras(f"Error al obtener datos de todas las FIBRAs: {str(e)}") 