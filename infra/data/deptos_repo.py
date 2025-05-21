import os
import joblib
import numpy as np
import pandas as pd
from typing import Dict, List, Any, Optional
from domain.exceptions import ModeloNoDisponible, FeatureNoValida, AlcaldiaNoEncontrada


class DepartamentosRepository:
    """Repositorio para manejar el modelo predictivo de departamentos"""
    
    def __init__(self):
        # Cargar el modelo y el scaler
        try:
            self.model = joblib.load('departamentos_model.joblib')
            self.scaler = joblib.load('departamentos_scaler.joblib')
            self.columns = joblib.load('departamentos_columns.joblib')
        except (FileNotFoundError, joblib.exceptions.JoblibException) as e:
            raise ModeloNoDisponible(f"departamentos: {str(e)}")
        
        # Lista de alcaldías conocidas por el modelo
        self.alcaldias = [col.replace('alcaldia_', '') for col in self.columns if col.startswith('alcaldia_')]
    
    def predict(self, input_data: Dict[str, Any]) -> float:
        """
        Realiza una predicción del precio del departamento
        
        Args:
            input_data: Diccionario con las características del departamento
            
        Returns:
            Precio predicho
        """
        # Crear un DataFrame con columnas que coincidan con las del modelo
        X = pd.DataFrame(columns=self.columns)
        X.loc[0] = 0  # Inicializar con ceros
        
        # Asignar valores numéricos básicos
        X.loc[0, 'metros_cuadrados'] = input_data['metros_cuadrados']
        X.loc[0, 'recamaras'] = input_data['recamaras']
        X.loc[0, 'banos'] = input_data['banos']
        X.loc[0, 'estacionamientos'] = input_data['estacionamientos']
        
        # Verificar que la alcaldía esté en las columnas del modelo
        alcaldia_col = f"alcaldia_{input_data['alcaldia']}"
        alcaldia_encontrada = False
        
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
        
        # Hacer predicción
        try:
            prediction = self.model.predict(X_scaled)[0]
            return prediction
        except Exception as e:
            raise FeatureNoValida(f"Error en la predicción: {str(e)}", None) 