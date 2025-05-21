from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from app.routers import casas_router, departamentos_router
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Verificar la clave API del INEGI
if not os.getenv("INEGI_API_KEY"):
    print("ADVERTENCIA: No se encontró la clave de API del INEGI. Crea un archivo .env con INEGI_API_KEY=tu_clave")

# Crear la aplicación
app = FastAPI(
    title="API de Predicción de Precios de Propiedades",
    description="API para predecir precios de casas y departamentos en la Ciudad de México",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar los orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir los routers
app.include_router(casas_router)
app.include_router(departamentos_router)


@app.get("/", tags=["root"])
async def root():
    """Endpoint raíz para verificar que la API está funcionando"""
    return {
        "message": "API de predicción de precios inmobiliarios",
        "endpoints": {
            "casas": "/casas/predict",
            "departamentos": "/departamentos/predict"
        }
    }


@app.get("/health", tags=["health"])
async def health_check():
    """Endpoint para verificar el estado de la API"""
    return {"status": "OK", "message": "El servicio está funcionando correctamente"} 