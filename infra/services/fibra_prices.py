import pandas as pd
from datetime import datetime
from domain.models import FibraPrecio
from domain.exceptions import ErrorFibras


class FibraPriceService:
    """Servicio para consultar precios de FIBRAs"""
    
    def __init__(self):
        try:
            self.df = pd.read_csv('fibras.csv')
            self.df['fecha'] = pd.to_datetime(self.df['fecha'])
            # Ordenar por fecha para facilitar el cálculo de variaciones
            self.df = self.df.sort_values('fecha')
        except Exception as e:
            raise ErrorFibras(f"Error al cargar datos: {str(e)}")

    def get_price(self, ticker: str) -> FibraPrecio:
        try:
            # Filtrar por ticker
            fibra_df = self.df[self.df['ticker'] == ticker].copy()
            if len(fibra_df) == 0:
                raise ErrorFibras(f"No se encontró la FIBRA: {ticker}")

            # Obtener el último registro
            ultimo_registro = fibra_df.iloc[-1]
            
            # Calcular la variación si hay más de un registro
            if len(fibra_df) > 1:
                registro_anterior = fibra_df.iloc[-2]
                variacion = ((ultimo_registro['precio'] - registro_anterior['precio']) / registro_anterior['precio']) * 100
            else:
                variacion = 0.0

            return FibraPrecio(
                ticker=ticker,
                precio=float(ultimo_registro['precio']),
                variacion=round(float(variacion), 2),
                fecha=ultimo_registro['fecha']
            )
        except Exception as e:
            raise ErrorFibras(f"Error al obtener precio de {ticker}: {str(e)}") 