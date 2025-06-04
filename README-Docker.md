# 🐳 Guía de Docker para Fennec ML API

Esta guía te ayudará a dockerizar y ejecutar tu aplicación de predicción de precios inmobiliarios.

## 📋 Prerrequisitos

- Docker instalado en tu sistema
- Docker Compose instalado

### Instalación de Docker (macOS)

```bash
# Opción 1: Descargar Docker Desktop desde https://www.docker.com/products/docker-desktop
# Opción 2: Usar Homebrew
brew install --cask docker
```

## 🚀 Comandos Rápidos

### Construcción y Ejecución

```bash
# Construir la imagen
make docker-build

# Ejecutar en modo producción
make docker-run

# Ejecutar en modo desarrollo (con hot-reload)
make docker-dev

# Ver logs
make docker-logs

# Detener contenedores
make docker-stop
```

### Comandos Docker Directos

```bash
# Construir imagen
docker build -t fennec-ml-api .

# Ejecutar contenedor simple
docker run -p 8000:8000 fennec-ml-api

# Ejecutar con docker-compose (producción)
docker-compose up -d

# Ejecutar con docker-compose (desarrollo)
docker-compose --profile dev up -d
```

## 📁 Estructura de Archivos Docker

```
├── Dockerfile              # Definición de la imagen
├── docker-compose.yml      # Orquestación de servicios
├── .dockerignore          # Archivos excluidos del build
└── README-Docker.md       # Esta guía
```

## 🔧 Configuración

### Dockerfile
- **Base**: Python 3.12.7 slim (coincide con tu versión local)
- **Puerto**: 8000
- **Usuario**: app (no-root para seguridad)
- **Dependencias**: Instaladas desde requirements.txt

### Docker Compose
- **fennec-ml-api**: Servicio de producción (puerto 8000)
- **fennec-ml-dev**: Servicio de desarrollo con hot-reload (puerto 8001)

## 🌐 Endpoints Disponibles

Una vez ejecutando, tu API estará disponible en:

- **Producción**: http://localhost:8000
- **Desarrollo**: http://localhost:8001
- **Documentación**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

### Endpoints principales:
- `GET /` - Información general de la API
- `POST /casas/predict` - Predicción de precios de casas
- `POST /departamentos/predict` - Predicción de precios de departamentos
- `GET /stats` - Estadísticas
- `GET /health` - Estado de la API

## 🛠️ Desarrollo

### Modo Desarrollo
```bash
# Ejecutar con hot-reload
make docker-dev

# Los cambios en el código se reflejarán automáticamente
# Disponible en http://localhost:8001
```

### Debugging
```bash
# Ver logs en tiempo real
make docker-logs

# Entrar al contenedor
docker exec -it fennec-ml-api bash

# Inspeccionar el contenedor
docker inspect fennec-ml-api
```

## 🧹 Limpieza

```bash
# Detener y limpiar todo
make docker-clean

# Limpiar sistema Docker completo
docker system prune -a --volumes
```

## 📊 Monitoreo

### Health Check
El contenedor incluye un health check que verifica:
- Respuesta del endpoint `/health`
- Intervalo: cada 30 segundos
- Timeout: 10 segundos
- Reintentos: 3

### Logs
```bash
# Ver logs del servicio
docker-compose logs fennec-ml-api

# Seguir logs en tiempo real
docker-compose logs -f fennec-ml-api
```

## 🚀 Despliegue en Producción

### Variables de Entorno
Crea un archivo `.env` para producción:

```env
# .env
PYTHONPATH=/app
ENVIRONMENT=production
LOG_LEVEL=info
```

### Docker Compose para Producción
```bash
# Ejecutar en modo producción
docker-compose up -d fennec-ml-api

# Verificar estado
docker-compose ps

# Escalar el servicio
docker-compose up -d --scale fennec-ml-api=3
```

## 🔍 Troubleshooting

### Problemas Comunes

1. **Puerto ocupado**
   ```bash
   # Cambiar puerto en docker-compose.yml
   ports:
     - "8080:8000"  # Usar puerto 8080 en lugar de 8000
   ```

2. **Modelos no encontrados**
   ```bash
   # Verificar que los archivos .joblib estén presentes
   ls -la *.joblib
   ```

3. **Permisos**
   ```bash
   # Dar permisos a los archivos de modelos
   chmod 644 *.joblib
   ```

4. **Memoria insuficiente**
   ```bash
   # Aumentar memoria de Docker Desktop
   # Settings > Resources > Memory > 4GB+
   ```

### Logs de Debug
```bash
# Ver logs detallados
docker-compose logs --tail=100 fennec-ml-api

# Ejecutar en modo interactivo
docker run -it --rm -p 8000:8000 fennec-ml-api bash
```

## 📈 Optimizaciones

### Imagen Multi-stage (Opcional)
Para reducir el tamaño de la imagen en producción, considera usar un Dockerfile multi-stage.

### Cache de Dependencias
El Dockerfile está optimizado para aprovechar el cache de Docker copiando `requirements.txt` primero.

### Seguridad
- Usuario no-root
- Archivos de solo lectura para modelos
- Exclusión de archivos sensibles con `.dockerignore`

---

¡Tu aplicación Fennec ML API está lista para Docker! 🎉 