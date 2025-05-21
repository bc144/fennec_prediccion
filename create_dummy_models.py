import joblib
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

# Crear columnas simuladas
casas_columns = [
    'metros_cuadrados', 'recamaras', 'banos', 'estacionamientos',
    'alcaldia_Alvaro Obregón', 'alcaldia_Azcapotzalco', 'alcaldia_Benito Juárez',
    'alcaldia_Coyoacán', 'alcaldia_Cuajimalpa de Morelos', 'alcaldia_Cuauhtémoc',
    'alcaldia_Gustavo A. Madero', 'alcaldia_Iztacalco', 'alcaldia_Iztapalapa',
    'alcaldia_La Magdalena Contreras', 'alcaldia_Miguel Hidalgo', 'alcaldia_Milpa Alta',
    'alcaldia_Tláhuac', 'alcaldia_Tlalpan', 'alcaldia_Venustiano Carranza',
    'alcaldia_Xochimilco'
]

departamentos_columns = casas_columns.copy()

# Crear modelos ficticios
print("Creando modelo simulado para casas...")
casas_model = RandomForestRegressor(n_estimators=10, random_state=42)
X_dummy = np.random.rand(100, len(casas_columns))
y_dummy = np.random.rand(100) * 10000000  # Precios en el rango de millones

# Entrenar el modelo con datos aleatorios
casas_model.fit(X_dummy, y_dummy)

# Crear y guardar un scaler ficticio
casas_scaler = StandardScaler()
casas_scaler.fit(X_dummy)

# Guardar los artefactos
joblib.dump(casas_model, 'casas_model.joblib')
joblib.dump(casas_scaler, 'casas_scaler.joblib')
joblib.dump(casas_columns, 'casas_columns.joblib')

print("Creando modelo simulado para departamentos...")
departamentos_model = RandomForestRegressor(n_estimators=10, random_state=42)
X_dummy = np.random.rand(100, len(departamentos_columns))
y_dummy = np.random.rand(100) * 8000000  # Precios en el rango de millones

# Entrenar el modelo con datos aleatorios
departamentos_model.fit(X_dummy, y_dummy)

# Crear y guardar un scaler ficticio
departamentos_scaler = StandardScaler()
departamentos_scaler.fit(X_dummy)

# Guardar los artefactos
joblib.dump(departamentos_model, 'departamentos_model.joblib')
joblib.dump(departamentos_scaler, 'departamentos_scaler.joblib')
joblib.dump(departamentos_columns, 'departamentos_columns.joblib')

print("Modelos simulados guardados exitosamente.") 