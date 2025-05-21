.PHONY: setup run test clean

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