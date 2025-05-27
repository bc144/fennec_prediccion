import pandas as pd
import numpy as np
import os
from typing import Dict, Any, List
from domain.exceptions import ErrorEstadisticas
from domain.models import PrecioM2Response, EstadisticasPrecios, TotalResponse, PreciosAlcaldiaResponse, PrecioM2AlcaldiaResponse


def _clean_numeric_data(value: str) -> float:
    """Limpia datos numéricos eliminando caracteres no numéricos y convirtiendo a float"""
    if pd.isna(value) or value == "No disponible" or value == "Bajó de precio":
        return np.nan
    
    if isinstance(value, (int, float)):
        return float(value)
    
    if isinstance(value, str):
        # Extraer solo los números y puntos decimales
        numeric_chars = ''.join(c for c in value if c.isdigit() or c == '.')
        if not numeric_chars:
            return np.nan
        try:
            return float(numeric_chars)
        except ValueError:
            return np.nan
    
    return np.nan


def _clean_area_data(value: str) -> float:
    """Limpia datos de área eliminando unidades y convirtiendo a float"""
    if pd.isna(value) or value == "No disponible":
        return np.nan
    
    if isinstance(value, (int, float)):
        return float(value)
    
    if isinstance(value, str):
        # Extraer solo los números antes de cualquier unidad
        parts = value.split()
        if not parts:
            return np.nan
        try:
            # Tomar el primer número que encontremos
            for part in parts:
                numeric_chars = ''.join(c for c in part if c.isdigit() or c == '.')
                if numeric_chars:
                    return float(numeric_chars)
            return np.nan
        except ValueError:
            return np.nan
    
    return np.nan


def remove_outliers(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Elimina outliers usando el método IQR"""
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]


class StatsRepository:
    """Repositorio para estadísticas de propiedades"""
    
    def __init__(self):
        try:
            # Obtener la ruta base del proyecto
            base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            
            # Cargar datos usando rutas absolutas
            self.casas_df = pd.read_csv(os.path.join(base_path, 'new_casas.csv'))
            self.deptos_df = pd.read_csv(os.path.join(base_path, 'new_departamentos.csv'))
            
            # Obtener lista de alcaldías
            self.alcaldias = [col.replace('alcaldia_', '') for col in self.casas_df.columns if col.startswith('alcaldia_')]
            
        except Exception as e:
            raise ErrorEstadisticas(f"Error al cargar datos: {str(e)}")
    
    def get_precio_m2_casas(self) -> PrecioM2Response:
        """Calcula el precio promedio por metro cuadrado de casas"""
        try:
            # Eliminar outliers y calcular el promedio
            df_clean = remove_outliers(self.casas_df, 'precio_por_mt2')
            precio_m2 = df_clean['precio_por_mt2'].mean()
            return PrecioM2Response(precio_m2=precio_m2)
        except Exception as e:
            raise ErrorEstadisticas(f"Error al calcular precio por m2: {str(e)}")
    
    def get_precio_m2_departamentos(self) -> PrecioM2Response:
        """Calcula el precio promedio por metro cuadrado de departamentos"""
        try:
            # Eliminar outliers y calcular el promedio
            df_clean = remove_outliers(self.deptos_df, 'precio_por_mt2')
            precio_m2 = df_clean['precio_por_mt2'].mean()
            return PrecioM2Response(precio_m2=precio_m2)
        except Exception as e:
            raise ErrorEstadisticas(f"Error al calcular precio por m2: {str(e)}")
    
    def get_stats_casas(self) -> EstadisticasPrecios:
        """Obtiene estadísticas de precios de casas"""
        try:
            # Eliminar outliers y calcular estadísticas
            df_clean = remove_outliers(self.casas_df, 'precio')
            stats = df_clean['precio'].describe()
            return EstadisticasPrecios(
                precio_minimo=float(stats['min']),
                precio_maximo=float(stats['max']),
                precio_promedio=float(stats['mean']),
                precio_mediana=float(stats['50%'])
            )
        except Exception as e:
            raise ErrorEstadisticas(f"Error al calcular estadísticas: {str(e)}")
    
    def get_stats_departamentos(self) -> EstadisticasPrecios:
        """Obtiene estadísticas de precios de departamentos"""
        try:
            # Eliminar outliers y calcular estadísticas
            df_clean = remove_outliers(self.deptos_df, 'precio')
            stats = df_clean['precio'].describe()
            return EstadisticasPrecios(
                precio_minimo=float(stats['min']),
                precio_maximo=float(stats['max']),
                precio_promedio=float(stats['mean']),
                precio_mediana=float(stats['50%'])
            )
        except Exception as e:
            raise ErrorEstadisticas(f"Error al calcular estadísticas: {str(e)}")
    
    def get_total_casas(self) -> TotalResponse:
        """Obtiene el total de casas"""
        return TotalResponse(total=len(self.casas_df))
    
    def get_total_departamentos(self) -> TotalResponse:
        """Obtiene el total de departamentos"""
        return TotalResponse(total=len(self.deptos_df))
    
    def get_total_propiedades(self) -> TotalResponse:
        """Obtiene el total de todas las propiedades"""
        return TotalResponse(total=len(self.casas_df) + len(self.deptos_df))

    def get_precio_promedio_por_alcaldia_casas(self) -> Dict[str, float]:
        """Obtiene el precio promedio por alcaldía para casas"""
        try:
            precios_por_alcaldia = {}
            for alcaldia in self.alcaldias:
                # Filtrar por alcaldía
                mask = self.casas_df[f'alcaldia_{alcaldia}'] == 1
                df_alcaldia = self.casas_df[mask]
                if len(df_alcaldia) > 0:
                    # Eliminar outliers y calcular promedio
                    df_clean = remove_outliers(df_alcaldia, 'precio')
                    precios_por_alcaldia[alcaldia] = float(df_clean['precio'].mean())
                else:
                    precios_por_alcaldia[alcaldia] = 0.0
            return precios_por_alcaldia
        except Exception as e:
            raise ErrorEstadisticas(f"Error al calcular precios por alcaldía: {str(e)}")

    def get_precio_promedio_por_alcaldia_departamentos(self) -> Dict[str, float]:
        """Obtiene el precio promedio por alcaldía para departamentos"""
        try:
            precios_por_alcaldia = {}
            for alcaldia in self.alcaldias:
                # Filtrar por alcaldía
                mask = self.deptos_df[f'alcaldia_{alcaldia}'] == 1
                df_alcaldia = self.deptos_df[mask]
                if len(df_alcaldia) > 0:
                    # Eliminar outliers y calcular promedio
                    df_clean = remove_outliers(df_alcaldia, 'precio')
                    precios_por_alcaldia[alcaldia] = float(df_clean['precio'].mean())
                else:
                    precios_por_alcaldia[alcaldia] = 0.0
            return precios_por_alcaldia
        except Exception as e:
            raise ErrorEstadisticas(f"Error al calcular precios por alcaldía: {str(e)}")

    def get_precio_m2_por_alcaldia_casas(self) -> Dict[str, float]:
        """Obtiene el precio promedio por metro cuadrado por alcaldía para casas"""
        try:
            precios_m2_por_alcaldia = {}
            for alcaldia in self.alcaldias:
                # Filtrar por alcaldía
                mask = self.casas_df[f'alcaldia_{alcaldia}'] == 1
                df_alcaldia = self.casas_df[mask]
                if len(df_alcaldia) > 0:
                    # Eliminar outliers y calcular promedio
                    df_clean = remove_outliers(df_alcaldia, 'precio_por_mt2')
                    precios_m2_por_alcaldia[alcaldia] = float(df_clean['precio_por_mt2'].mean())
                else:
                    precios_m2_por_alcaldia[alcaldia] = 0.0
            return precios_m2_por_alcaldia
        except Exception as e:
            raise ErrorEstadisticas(f"Error al calcular precios por m2 por alcaldía: {str(e)}")

    def get_precio_m2_por_alcaldia_departamentos(self) -> Dict[str, float]:
        """Obtiene el precio promedio por metro cuadrado por alcaldía para departamentos"""
        try:
            precios_m2_por_alcaldia = {}
            for alcaldia in self.alcaldias:
                # Filtrar por alcaldía
                mask = self.deptos_df[f'alcaldia_{alcaldia}'] == 1
                df_alcaldia = self.deptos_df[mask]
                if len(df_alcaldia) > 0:
                    # Eliminar outliers y calcular promedio
                    df_clean = remove_outliers(df_alcaldia, 'precio_por_mt2')
                    precios_m2_por_alcaldia[alcaldia] = float(df_clean['precio_por_mt2'].mean())
                else:
                    precios_m2_por_alcaldia[alcaldia] = 0.0
            return precios_m2_por_alcaldia
        except Exception as e:
            raise ErrorEstadisticas(f"Error al calcular precios por m2 por alcaldía: {str(e)}")

    def get_precio_m2_por_alcaldia_total(self) -> Dict[str, float]:
        """Obtiene el precio promedio por metro cuadrado por alcaldía para todas las propiedades"""
        try:
            precios_m2_por_alcaldia = {}
            for alcaldia in self.alcaldias:
                # Filtrar casas por alcaldía
                mask_casas = self.casas_df[f'alcaldia_{alcaldia}'] == 1
                df_casas = self.casas_df[mask_casas]
                
                # Filtrar departamentos por alcaldía
                mask_deptos = self.deptos_df[f'alcaldia_{alcaldia}'] == 1
                df_deptos = self.deptos_df[mask_deptos]
                
                # Combinar datos
                df_combined = pd.concat([
                    df_casas[['precio_por_mt2']],
                    df_deptos[['precio_por_mt2']]
                ])
                
                if len(df_combined) > 0:
                    # Eliminar outliers y calcular promedio
                    df_clean = remove_outliers(df_combined, 'precio_por_mt2')
                    precios_m2_por_alcaldia[alcaldia] = float(df_clean['precio_por_mt2'].mean())
                else:
                    precios_m2_por_alcaldia[alcaldia] = 0.0
                    
            return precios_m2_por_alcaldia
        except Exception as e:
            raise ErrorEstadisticas(f"Error al calcular precios por m2 por alcaldía: {str(e)}")

    def get_precio_promedio_por_alcaldia_total(self) -> Dict[str, float]:
        """Obtiene el precio promedio por alcaldía para todas las propiedades"""
        try:
            precios_por_alcaldia = {}
            for alcaldia in self.alcaldias:
                # Filtrar casas por alcaldía
                mask_casas = self.casas_df[f'alcaldia_{alcaldia}'] == 1
                df_casas = self.casas_df[mask_casas]
                
                # Filtrar departamentos por alcaldía
                mask_deptos = self.deptos_df[f'alcaldia_{alcaldia}'] == 1
                df_deptos = self.deptos_df[mask_deptos]
                
                # Combinar datos
                df_combined = pd.concat([
                    df_casas[['precio']],
                    df_deptos[['precio']]
                ])
                
                if len(df_combined) > 0:
                    # Eliminar outliers y calcular promedio
                    df_clean = remove_outliers(df_combined, 'precio')
                    precios_por_alcaldia[alcaldia] = float(df_clean['precio'].mean())
                else:
                    precios_por_alcaldia[alcaldia] = 0.0
                    
            return precios_por_alcaldia
        except Exception as e:
            raise ErrorEstadisticas(f"Error al calcular precios por alcaldía: {str(e)}") 