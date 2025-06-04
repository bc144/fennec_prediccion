# 🚀 Despliegue en Render - Fennec ML API

Guía completa para desplegar tu API de predicción de precios inmobiliarios en Render.

## 🌟 ¿Por qué Render?

- ✅ **Fácil de usar** - Conecta tu repo y despliega automáticamente
- ✅ **Plan gratuito** - 750 horas gratis al mes
- ✅ **Docker nativo** - Detecta tu Dockerfile automáticamente
- ✅ **SSL automático** - HTTPS incluido
- ✅ **Auto-deploy** - Se actualiza con cada push

## 📋 Prerrequisitos

1. Cuenta en [render.com](https://render.com)
2. Tu código en GitHub/GitLab
3. Los archivos Docker ya están listos ✅

## 🚀 Pasos para Desplegar

### 1. Hacer Push de tu Código

```bash
# Agregar todos los archivos
git add .

# Commit
git commit -m "Add Docker configuration for Render deployment"

# Push a tu repositorio
git push
```

### 2. Crear Servicio en Render

1. **Ve a [render.com](https://render.com)** y haz login
2. **Click en "New +"** → **"Web Service"**
3. **Conecta tu repositorio** de GitHub/GitLab
4. **Selecciona tu repo** `modelos_fennec`

### 3. Configuración del Servicio

Render detectará automáticamente tu Dockerfile, pero verifica:

- **Name**: `fennec-ml-api`
- **Environment**: `Docker`
- **Region**: `Oregon (US West)` (más barato)
- **Branch**: `main` o tu rama principal
- **Dockerfile Path**: `./Dockerfile` ✅
- **Build Command**: (dejar vacío)
- **Start Command**: (dejar vacío, usa el CMD del Dockerfile)

### 4. Variables de Entorno (Opcional)

En la sección "Environment Variables":
- `PYTHONPATH` = `/app`
- `PORT` = `8000` (Render lo maneja automáticamente)

### 5. Plan de Servicio

- **Free Plan**: ✅ Perfecto para empezar
  - 750 horas gratis/mes
  - Se "duerme" después de 15 min sin uso
  - Despierta automáticamente con requests

## 🌐 Después del Despliegue

### Tu API estará disponible en:
```
https://fennec-ml-api.onrender.com
```

### Endpoints disponibles:
- `GET /` - Información general
- `GET /docs` - Documentación Swagger
- `GET /health` - Health check
- `POST /casas/predict` - Predicción de casas
- `POST /departamentos/predict` - Predicción de departamentos

## 🔧 Configuración Avanzada (Opcional)

### Auto-Deploy
- ✅ Ya configurado en `render.yaml`
- Cada push a tu rama principal despliega automáticamente

### Health Check
- ✅ Configurado en `/health`
- Render verificará que tu API esté funcionando

### Logs
- Ve a tu dashboard en Render
- Click en tu servicio → "Logs"
- Logs en tiempo real de tu aplicación

## 🐛 Troubleshooting

### Problemas Comunes

1. **Build falla**
   ```bash
   # Verifica que requirements.txt esté presente
   ls requirements.txt
   ```

2. **Modelos no encontrados**
   ```bash
   # Verifica que los .joblib estén en el repo
   ls *.joblib
   ```

3. **Puerto incorrecto**
   - Render maneja el puerto automáticamente
   - Tu Dockerfile ya está configurado correctamente

4. **Servicio se "duerme"**
   - Normal en plan gratuito
   - Se despierta automáticamente (puede tardar ~30 segundos)

### Ver Logs
1. Dashboard de Render → Tu servicio
2. Tab "Logs"
3. Logs en tiempo real

## 💰 Costos

### Plan Gratuito
- **750 horas/mes gratis**
- **Se duerme después de 15 min** sin actividad
- **Perfecto para desarrollo y demos**

### Plan Starter ($7/mes)
- **Siempre activo** (no se duerme)
- **Mejor para producción**

## 🔄 Actualizaciones

```bash
# Hacer cambios en tu código
git add .
git commit -m "Update API"
git push

# Render desplegará automáticamente 🚀
```

## 📊 Monitoreo

### Dashboard de Render
- **Métricas de uso**
- **Logs en tiempo real**
- **Estado del servicio**
- **Historial de deploys**

### Health Check
- Render verifica `/health` automáticamente
- Si falla, reinicia el servicio

## 🎯 Próximos Pasos

1. **Haz push** de tu código
2. **Crea el servicio** en Render
3. **¡Tu API estará live!** 🎉

### Ejemplo de uso:
```bash
# Probar tu API desplegada
curl https://fennec-ml-api.onrender.com/health

# Ver documentación
# https://fennec-ml-api.onrender.com/docs
```

---

¡Tu API Fennec ML estará disponible en internet en minutos! 🚀 