import os
import joblib
import numpy as np
import pandas as pd
from typing import Dict, List, Any, Optional
from domain.exceptions import ModeloNoDisponible, FeatureNoValida, AlcaldiaNoEncontrada


class CasasRepository:
    """Repositorio para manejar el modelo predictivo de casas"""
    
    def __init__(self):
        # Cargar el modelo y el scaler
        try:
            self.model = joblib.load('casas_model.joblib')
            self.scaler = joblib.load('casas_scaler.joblib')
            self.columns = joblib.load('casas_columns.joblib')
        except (FileNotFoundError, joblib.exceptions.JoblibException) as e:
            raise ModeloNoDisponible(f"casas: {str(e)}")
        
        # Lista de alcaldías conocidas por el modelo
        self.alcaldias = [col.replace('alcaldia_', '') for col in self.columns if col.startswith('alcaldia_')]
        
        # Límites para valores numéricos (basados en el análisis de datos)
        self.limits = {
            'dimensiones': (20, 1000),  # m2 mínimos y máximos razonables
            'recamaras': (1, 10),       # número de recámaras razonable
            'banos': (1, 8),            # número de baños razonable
            'estacionamientos': (0, 6)  # número de estacionamientos razonable
        }
    
    def _validate_numeric_input(self, feature: str, value: float) -> None:
        """Valida que un valor numérico esté dentro de los límites razonables"""
        if feature in self.limits:
            min_val, max_val = self.limits[feature]
            if value < min_val or value > max_val:
                raise FeatureNoValida(
                    f"El valor {value} para {feature} está fuera del rango válido ({min_val}, {max_val})",
                    feature
                )
    
    def predict(self, input_data: Dict[str, Any]) -> float:
        """
        Realiza una predicción del precio de la casa
        
        Args:
            input_data: Diccionario con las características de la casa
            
        Returns:
            Precio predicho
            
        Raises:
            AlcaldiaNoEncontrada: Si la alcaldía no está en el modelo
            FeatureNoValida: Si algún valor está fuera de rango
            ModeloNoDisponible: Si hay un error con el modelo
        """
        try:
            # Convertir metros_cuadrados a dimensiones
            input_data['dimensiones'] = input_data.pop('metros_cuadrados')
            
            # Validar valores numéricos
            for feature in ['dimensiones', 'recamaras', 'banos', 'estacionamientos']:
                self._validate_numeric_input(feature, float(input_data[feature]))
            
            # Crear un DataFrame con columnas que coincidan con las del modelo
            X = pd.DataFrame(columns=self.columns)
            X.loc[0] = 0  # Inicializar con ceros
            
            # Asignar valores numéricos
            X.loc[0, 'dimensiones'] = input_data['dimensiones']
            X.loc[0, 'recamaras'] = input_data['recamaras']
            X.loc[0, 'banos'] = input_data['banos']
            X.loc[0, 'estacionamientos'] = input_data['estacionamientos']
            
            # Verificar que la alcaldía esté en las columnas del modelo
            alcaldia = input_data['alcaldia']
            alcaldia_col = f"alcaldia_{alcaldia}"
            alcaldia_encontrada = False
            
            # Debug: imprimir alcaldías disponibles
            print(f"Alcaldías disponibles: {self.alcaldias}")
            print(f"Alcaldía recibida: {alcaldia}")
            print(f"Buscando columna: {alcaldia_col}")
            
            for col in self.columns:
                if col.startswith('alcaldia_'):
                    if col == alcaldia_col:
                        X.loc[0, col] = 1
                        alcaldia_encontrada = True
                    else:
                        X.loc[0, col] = 0
            
            if not alcaldia_encontrada:
                raise AlcaldiaNoEncontrada(input_data['alcaldia'])
            
            # Aplicar el escalador
            X_scaled = self.scaler.transform(X)
            
            # Hacer predicción (el modelo devuelve el logaritmo del precio)
            log_prediction = self.model.predict(X_scaled)[0]
            
            # Convertir de logaritmo a precio real y redondear a 2 decimales
            prediction = float(np.exp(log_prediction))
            print(f"Log prediction: {log_prediction}")
            print(f"Final prediction: {prediction}")
            
            return prediction
            
        except AlcaldiaNoEncontrada:
            raise
        except FeatureNoValida:
            raise
        except Exception as e:
            raise ModeloNoDisponible(f"Error en la predicción: {str(e)}") 