import yfinance as yf
import pandas as pd
from typing import List, Dict
from domain.models import FibraResponse
from domain.exceptions import ErrorFibras
from datetime import datetime, timedelta
import requests
import time

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
            print(f"Intentando obtener datos para {nombre} ({ticker})")
            
            # Configurar timeout y reintentos para producción
            max_retries = 3
            timeout = 30
            
            for attempt in range(max_retries):
                try:
                    print(f"Intento {attempt + 1} para {nombre}")
                    
                    # Crear ticker con configuración específica para producción
                    fibra = yf.Ticker(ticker)
                    
                    # Intentar con diferentes períodos si falla
                    periods = ["5d", "1mo", "3mo"]
                    hist = None
                    
                    for period in periods:
                        try:
                            print(f"Probando período {period} para {nombre}")
                            hist = fibra.history(period=period, timeout=timeout)
                            if len(hist) > 0:
                                print(f"Datos obtenidos con período {period} para {nombre}")
                                break
                        except Exception as period_error:
                            print(f"Error con período {period} para {nombre}: {str(period_error)}")
                            continue
                    
                    if hist is None or len(hist) == 0:
                        if attempt < max_retries - 1:
                            print(f"Sin datos en intento {attempt + 1}, reintentando en 2 segundos...")
                            time.sleep(2)
                            continue
                        else:
                            raise ErrorFibras(f"No hay datos disponibles para {nombre} después de {max_retries} intentos")
                    
                    # Obtener el último precio
                    ultimo_precio = hist['Close'].iloc[-1]
                    print(f"Último precio para {nombre}: {ultimo_precio}")
                    
                    # Calcular la variación si hay más de un precio
                    if len(hist) > 1:
                        precio_anterior = hist['Close'].iloc[-2]
                        variacion = ((ultimo_precio - precio_anterior) / precio_anterior) * 100
                    else:
                        variacion = 0.0
                    
                    print(f"Variación calculada para {nombre}: {variacion}%")
                    
                    return FibraResponse(
                        nombre=nombre,
                        precio=round(float(ultimo_precio), 2),
                        variacion=round(float(variacion), 2),
                        fecha=hist.index[-1].strftime('%Y-%m-%d')
                    )
                    
                except requests.exceptions.Timeout:
                    print(f"Timeout en intento {attempt + 1} para {nombre}")
                    if attempt < max_retries - 1:
                        time.sleep(2)
                        continue
                    else:
                        raise ErrorFibras(f"Timeout al obtener datos de {nombre}")
                        
                except requests.exceptions.ConnectionError:
                    print(f"Error de conexión en intento {attempt + 1} para {nombre}")
                    if attempt < max_retries - 1:
                        time.sleep(2)
                        continue
                    else:
                        raise ErrorFibras(f"Error de conexión al obtener datos de {nombre}")
                        
                except Exception as e:
                    print(f"Error en intento {attempt + 1} para {nombre}: {str(e)}")
                    if attempt < max_retries - 1:
                        time.sleep(2)
                        continue
                    else:
                        raise ErrorFibras(f"Error al obtener datos de {nombre}: {str(e)}")
            
        except ErrorFibras:
            raise
        except Exception as e:
            print(f"Error general para {nombre}: {str(e)}")
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
            print("Iniciando obtención de datos de todas las FIBRAs")
            fibras_data = []
            errors = []
            
            for nombre in self.fibras.keys():
                try:
                    print(f"Procesando FIBRA: {nombre}")
                    fibra_data = self.get_fibra(nombre)
                    fibras_data.append(fibra_data)
                    print(f"FIBRA {nombre} procesada exitosamente")
                except ErrorFibras as e:
                    error_msg = f"Error en {nombre}: {str(e)}"
                    print(error_msg)
                    errors.append(error_msg)
                    continue
            
            if not fibras_data:
                error_detail = f"No se pudieron obtener datos de ninguna FIBRA. Errores: {'; '.join(errors)}"
                print(error_detail)
                raise ErrorFibras(error_detail)
            
            print(f"Se obtuvieron datos de {len(fibras_data)} FIBRAs exitosamente")
            return fibras_data
            
        except ErrorFibras:
            raise
        except Exception as e:
            print(f"Error general al obtener todas las FIBRAs: {str(e)}")
            raise ErrorFibras(f"Error al obtener datos de todas las FIBRAs: {str(e)}") 