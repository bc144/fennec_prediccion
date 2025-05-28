import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import joblib

# Función principal para entrenar modelos
def train_models():
    print("Entrenando modelo para casas...")
    # Cargar datos de casas
    casas_df = pd.read_csv('new_casas.csv')
    
    # Seleccionar características para el modelo
    feature_cols = ['dimensiones', 'recamaras', 'banos', 'estacionamientos']
    casas_alcaldia_cols = [col for col in casas_df.columns if col.startswith('alcaldia_')]
    casas_features = casas_df[feature_cols + casas_alcaldia_cols]
    casas_target = casas_df['log_precio']  # Usamos el logaritmo del precio
    
    # Dividir en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(casas_features, casas_target, test_size=0.2, random_state=42)
    
    # Escalar características
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Guardar el scaler
    joblib.dump(scaler, 'casas_scaler.joblib')
    
    # Entrenar el modelo
    model = LinearRegression()
    model.fit(X_train_scaled, y_train)
    
    # Evaluar el modelo
    score = model.score(X_test_scaled, y_test)
    print(f"R² para casas: {score:.4f}")
    
    # Guardar el modelo
    joblib.dump(model, 'casas_model.joblib')
    
    # Guardar las columnas para referencia
    column_names = X_train.columns.tolist()
    joblib.dump(column_names, 'casas_columns.joblib')
    
    print("Entrenando modelo para departamentos...")
    # Cargar datos de departamentos
    deptos_df = pd.read_csv('new_departamentos.csv')
    
    # Seleccionar características para el modelo
    deptos_alcaldia_cols = [col for col in deptos_df.columns if col.startswith('alcaldia_')]
    deptos_features = deptos_df[feature_cols + deptos_alcaldia_cols]
    deptos_target = deptos_df['log_precio']  # Usamos el logaritmo del precio
    
    # Dividir en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(deptos_features, deptos_target, test_size=0.2, random_state=42)
    
    # Escalar características
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Guardar el scaler
    joblib.dump(scaler, 'departamentos_scaler.joblib')
    
    # Entrenar el modelo
    model = LinearRegression()
    model.fit(X_train_scaled, y_train)
    
    # Evaluar el modelo
    score = model.score(X_test_scaled, y_test)
    print(f"R² para departamentos: {score:.4f}")
    
    # Guardar el modelo
    joblib.dump(model, 'departamentos_model.joblib')
    
    # Guardar las columnas para referencia
    column_names = X_train.columns.tolist()
    joblib.dump(column_names, 'departamentos_columns.joblib')
    
    print("Modelos guardados exitosamente.")

if __name__ == "__main__":
    train_models() 