.PHONY: setup run test clean docker-build docker-run docker-dev docker-stop docker-clean docker-logs docker-rebuild

# Configuración del entorno
setup:
	python -m pip install --upgrade pip
	pip install -r requirements.txt

# Ejecutar la aplicación
run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Ejecutar pruebas
test:
	pytest tests/ -v

# Limpiar archivos temporales
clean:
	rm -rf __pycache__
	rm -rf */__pycache__
	rm -rf */*/__pycache__
	rm -rf */*/*/__pycache__
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf htmlcov

# === COMANDOS DOCKER ===

# Construir la imagen Docker
docker-build:
	docker build -t fennec-ml-api .

# Ejecutar con Docker (producción)
docker-run:
	docker-compose up -d fennec-ml-api

# Ejecutar con Docker (desarrollo con hot-reload)
docker-dev:
	docker-compose --profile dev up -d fennec-ml-dev

# Detener contenedores
docker-stop:
	docker-compose down

# Limpiar imágenes y contenedores Docker
docker-clean:
	docker-compose down --rmi all --volumes --remove-orphans
	docker system prune -f

# Ver logs
docker-logs:
	docker-compose logs -f

# Reconstruir y ejecutar
docker-rebuild:
	docker-compose down
	docker-compose build --no-cache
	docker-compose up -d 