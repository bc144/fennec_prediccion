import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import joblib
import re

# Función para limpiar y preparar los datos
def clean_numeric_column(df, column):
    # Extraer solo valores numéricos
    df[column] = df[column].str.extract(r'(\d+)').astype(float)
    return df

# Función para transformar columnas categóricas
def prepare_categorical(df, column, prefix):
    # Crear variables dummy
    dummies = pd.get_dummies(df[column], prefix=prefix)
    df = pd.concat([df, dummies], axis=1)
    df = df.drop(column, axis=1)
    return df

# Función principal para entrenar modelos
def train_models():
    print("Entrenando modelo para casas...")
    # Cargar datos de casas
    casas_df = pd.read_csv('casas.csv')
    
    # Limpiar columnas
    casas_df = casas_df.drop_duplicates()
    casas_df['price_numeric'] = casas_df['price'].str.extract(r'(\d+(?:,\d+)*(?:\.\d+)?)')
    casas_df['price_numeric'] = casas_df['price_numeric'].str.replace(',', '').astype(float)
    
    # Extraer alcaldía desde la columna 'col'
    casas_df['alcaldia'] = casas_df['col'].apply(lambda x: x.split(',')[-1].strip() if isinstance(x, str) and ',' in x else 'Desconocida')
    
    # Limpiar y convertir columnas numéricas
    for col in ['recamaras', 'banos', 'estacionamientos']:
        casas_df = clean_numeric_column(casas_df, col)
    
    # Extraer metros cuadrados desde terreno
    casas_df['metros_cuadrados'] = pd.to_numeric(casas_df['terreno'].str.extract(r'(\d+)')[0], errors='coerce')
    
    # Eliminar filas con valores nulos
    casas_df = casas_df.dropna(subset=['price_numeric', 'metros_cuadrados', 'recamaras', 'banos', 'estacionamientos'])
    
    # Aplicar transformación logarítmica a los precios
    casas_df['log_price'] = np.log(casas_df['price_numeric'])
    
    # Seleccionar características para el modelo
    casas_features = casas_df[['metros_cuadrados', 'recamaras', 'banos', 'estacionamientos', 'alcaldia']]
    casas_target = casas_df['log_price']  # Usamos el precio logarítmico
    
    # Preparar variables categóricas
    casas_features = prepare_categorical(casas_features, 'alcaldia', 'alcaldia')
    
    # Dividir en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(casas_features, casas_target, test_size=0.2, random_state=42)
    
    # Escalar características
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Guardar el scaler
    joblib.dump(scaler, 'casas_scaler.joblib')
    
    # Entrenar el modelo
    model = RandomForestRegressor(n_estimators=100, random_state=42)
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
    deptos_df = pd.read_csv('departamentos.csv')
    
    # Limpiar columnas
    deptos_df = deptos_df.drop_duplicates()
    deptos_df['price_numeric'] = deptos_df['price'].str.extract(r'(\d+(?:,\d+)*(?:\.\d+)?)')
    deptos_df['price_numeric'] = deptos_df['price_numeric'].str.replace(',', '').astype(float)
    
    # Extraer alcaldía desde la columna 'col'
    deptos_df['alcaldia'] = deptos_df['col'].apply(lambda x: x.split(',')[-1].strip() if isinstance(x, str) and ',' in x else 'Desconocida')
    
    # Limpiar y convertir columnas numéricas
    for col in ['recamaras', 'banos', 'estacionamientos']:
        deptos_df = clean_numeric_column(deptos_df, col)
    
    # Extraer metros cuadrados desde terreno
    deptos_df['metros_cuadrados'] = pd.to_numeric(deptos_df['terreno'].str.extract(r'(\d+)')[0], errors='coerce')
    
    # Eliminar filas con valores nulos
    deptos_df = deptos_df.dropna(subset=['price_numeric', 'metros_cuadrados', 'recamaras', 'banos', 'estacionamientos'])
    
    # Aplicar transformación logarítmica a los precios
    deptos_df['log_price'] = np.log(deptos_df['price_numeric'])
    
    # Seleccionar características para el modelo
    deptos_features = deptos_df[['metros_cuadrados', 'recamaras', 'banos', 'estacionamientos', 'alcaldia']]
    deptos_target = deptos_df['log_price']  # Usamos el precio logarítmico
    
    # Preparar variables categóricas
    deptos_features = prepare_categorical(deptos_features, 'alcaldia', 'alcaldia')
    
    # Dividir en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(deptos_features, deptos_target, test_size=0.2, random_state=42)
    
    # Escalar características
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Guardar el scaler
    joblib.dump(scaler, 'departamentos_scaler.joblib')
    
    # Entrenar el modelo
    model = RandomForestRegressor(n_estimators=100, random_state=42)
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