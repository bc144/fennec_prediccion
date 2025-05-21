<<<<<<< HEAD
# fennec_ml
Modelo de Regresión Lineal de Fennec 

# API de Predicción de Precios Inmobiliarios

Servicio RESTful para predecir el valor de propiedades (casas y departamentos) en la Ciudad de México utilizando FastAPI y modelos de Machine Learning.

## Estructura del Proyecto

El proyecto sigue los principios de Clean Architecture:

- **domain/**: Modelos y excepciones de dominio
- **infra/**: Implementaciones de infraestructura (repositorios y servicios)
- **usecases/**: Casos de uso de la aplicación
- **app/**: Aplicación FastAPI y routers
- **tests/**: Pruebas unitarias

## Requisitos

- Python 3.8+
- Las dependencias listadas en `requirements.txt`

## Configuración

1. Clonar el repositorio:

```bash
git clone <url-del-repositorio>
cd modelos_fennec
```

2. Crear un entorno virtual:

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
```

3. Instalar dependencias:

```bash
make setup  # Alternativa: pip install -r requirements.txt
```

4. Configurar la clave API del INEGI:

Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```
INEGI_API_KEY=tu_clave_de_api_aqui
```

## Ejecución

Para iniciar el servidor de desarrollo:

```bash
make run  # Alternativa: uvicorn app.main:app --reload
```

El servidor estará disponible en http://localhost:8000

## Documentación de la API

La documentación interactiva estará disponible en:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Ejemplos de Uso

### Predecir el precio de una casa

```bash
curl -X 'POST' \
  'http://localhost:8000/casas/predict' \
  -H 'Content-Type: application/json' \
  -d '{
  "alcaldia": "Benito Juárez",
  "metros_cuadrados": 150,
  "recamaras": 3,
  "banos": 2,
  "estacionamientos": 1
}'
```

### Predecir el precio de un departamento

```bash
curl -X 'POST' \
  'http://localhost:8000/departamentos/predict' \
  -H 'Content-Type: application/json' \
  -d '{
  "alcaldia": "Miguel Hidalgo",
  "metros_cuadrados": 80,
  "recamaras": 2,
  "banos": 1,
  "estacionamientos": 1
}'
```

## Pruebas

Para ejecutar las pruebas unitarias:

```bash
make test  # Alternativa: pytest tests/ -v
```

## Licencia

Este proyecto está licenciado bajo la licencia MIT. 
>>>>>>> 51b087b (Initial commit for fennec_ml)
