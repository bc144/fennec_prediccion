import pandas as pd
from typing import Dict, List
from domain.exceptions import ErrorEstadisticas


class StatsRepository:
    """Repositorio para manejar estadísticas de propiedades"""
    
    def __init__(self):
        try:
            # Cargar los datasets
            self.casas_df = pd.read_json('casas.json')
            self.departamentos_df = pd.read_json('departamentos.json')
            
            # Procesar los datos
            self._procesar_datos()
        except Exception as e:
            raise ErrorEstadisticas(f"Error al cargar datos: {str(e)}")
    
    def _procesar_datos(self):
        """Preprocesa los dataframes para cálculos posteriores"""
        # Procesar casas
        self.casas_df['precio'] = self.casas_df['price'].str.extract(r'MN\s*([\d,]+)').astype(float)
        self.casas_df['metros_cuadrados'] = self.casas_df['terreno'].str.extract(r'(\d+)').astype(float)
        
        # Procesar departamentos
        self.departamentos_df['precio'] = self.departamentos_df['price'].str.extract(r'MN\s*([\d,]+)').astype(float)
        self.departamentos_df['metros_cuadrados'] = self.departamentos_df['terreno'].str.extract(r'(\d+)').astype(float)
    
    def get_precio_m2_casas(self) -> float:
        """Calcula el precio promedio por metro cuadrado para casas"""
        try:
            return (self.casas_df['precio'] / self.casas_df['metros_cuadrados']).mean()
        except Exception as e:
            raise ErrorEstadisticas(f"Error al calcular precio por m2 de casas: {str(e)}")
    
    def get_precio_m2_departamentos(self) -> float:
        """Calcula el precio promedio por metro cuadrado para departamentos"""
        try:
            return (self.departamentos_df['precio'] / self.departamentos_df['metros_cuadrados']).mean()
        except Exception as e:
            raise ErrorEstadisticas(f"Error al calcular precio por m2 de departamentos: {str(e)}")
    
    def get_stats_casas(self) -> Dict[str, float]:
        """Obtiene estadísticas de precios para casas"""
        try:
            return {
                'precio_minimo': self.casas_df['precio'].min(),
                'precio_maximo': self.casas_df['precio'].max(),
                'precio_promedio': self.casas_df['precio'].mean(),
                'precio_mediana': self.casas_df['precio'].median()
            }
        except Exception as e:
            raise ErrorEstadisticas(f"Error al calcular estadísticas de casas: {str(e)}")
    
    def get_stats_departamentos(self) -> Dict[str, float]:
        """Obtiene estadísticas de precios para departamentos"""
        try:
            return {
                'precio_minimo': self.departamentos_df['precio'].min(),
                'precio_maximo': self.departamentos_df['precio'].max(),
                'precio_promedio': self.departamentos_df['precio'].mean(),
                'precio_mediana': self.departamentos_df['precio'].median()
            }
        except Exception as e:
            raise ErrorEstadisticas(f"Error al calcular estadísticas de departamentos: {str(e)}")
    
    def get_total_casas(self) -> int:
        """Obtiene el total de casas"""
        try:
            return len(self.casas_df)
        except Exception as e:
            raise ErrorEstadisticas(f"Error al obtener total de casas: {str(e)}")
    
    def get_total_departamentos(self) -> int:
        """Obtiene el total de departamentos"""
        try:
            return len(self.departamentos_df)
        except Exception as e:
            raise ErrorEstadisticas(f"Error al obtener total de departamentos: {str(e)}")
    
    def get_total_propiedades(self) -> int:
        """Obtiene el total de propiedades"""
        try:
            return len(self.casas_df) + len(self.departamentos_df)
        except Exception as e:
            raise ErrorEstadisticas(f"Error al obtener total de propiedades: {str(e)}") 