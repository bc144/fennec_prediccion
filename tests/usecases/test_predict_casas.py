import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime
from domain.models import CasaInputData, Prediccion, UrbanRate
from domain.exceptions import AlcaldiaNoEncontrada, ModeloNoDisponible
from usecases.predict_casas import predict_casa


class TestPredictCasaUseCase:
    """Pruebas para el caso de uso de predicción de casas"""
    
    @patch("usecases.predict_casas.get_urban_rate")
    @patch("usecases.predict_casas.CasasRepository")
    def test_predict_casa_success(self, mock_repo_class, mock_get_urban_rate):
        """Test para verificar una predicción exitosa"""
        # Configurar los mocks
        mock_urban_rate = UrbanRate(
            alcaldia="Benito Juárez",
            poblacion_total=100000,
            poblacion_urbana=95000,
            tasa_urbanizacion=0.95
        )
        mock_get_urban_rate.return_value = mock_urban_rate
        
        mock_repo = mock_repo_class.return_value
        mock_repo.predict.return_value = 5000000.0
        
        # Crear los datos de entrada
        input_data = CasaInputData(
            alcaldia="Benito Juárez",
            metros_cuadrados=150,
            recamaras=3,
            banos=2,
            estacionamientos=1
        )
        
        # Ejecutar el caso de uso
        result = predict_casa(input_data)
        
        # Verificar el resultado
        assert isinstance(result, Prediccion)
        assert result.tipo_propiedad == "casa"
        assert result.precio_estimado == 5000000.0
        assert result.alcaldia == "Benito Juárez"
        assert result.tasa_urbanizacion == 0.95
        assert result.caracteristicas == {
            'metros_cuadrados': 150,
            'recamaras': 3,
            'banos': 2,
            'estacionamientos': 1
        }
        # Verificar que la fecha es válida
        datetime.fromisoformat(result.fecha_prediccion)
        
        # Verificar que se llamaron los métodos correctos
        mock_get_urban_rate.assert_called_once_with("Benito Juárez")
        mock_repo.predict.assert_called_once()
    
    @patch("usecases.predict_casas.get_urban_rate")
    @patch("usecases.predict_casas.CasasRepository")
    def test_predict_casa_alcaldia_no_encontrada(self, mock_repo_class, mock_get_urban_rate):
        """Test para verificar el manejo de alcaldías no encontradas"""
        # Configurar los mocks
        mock_get_urban_rate.side_effect = AlcaldiaNoEncontrada("Alcaldía Inexistente")
        
        # Crear los datos de entrada
        input_data = CasaInputData(
            alcaldia="Alcaldía Inexistente",
            metros_cuadrados=150,
            recamaras=3,
            banos=2,
            estacionamientos=1
        )
        
        # Verificar que se propaga la excepción
        with pytest.raises(AlcaldiaNoEncontrada):
            predict_casa(input_data)
        
        # Verificar que no se llamó al repositorio
        mock_repo_class.assert_not_called()
    
    @patch("usecases.predict_casas.get_urban_rate")
    @patch("usecases.predict_casas.CasasRepository")
    def test_predict_casa_modelo_no_disponible(self, mock_repo_class, mock_get_urban_rate):
        """Test para verificar el manejo de modelos no disponibles"""
        # Configurar los mocks
        mock_urban_rate = UrbanRate(
            alcaldia="Benito Juárez",
            poblacion_total=100000,
            poblacion_urbana=95000,
            tasa_urbanizacion=0.95
        )
        mock_get_urban_rate.return_value = mock_urban_rate
        
        mock_repo_class.side_effect = ModeloNoDisponible("casas: archivo no encontrado")
        
        # Crear los datos de entrada
        input_data = CasaInputData(
            alcaldia="Benito Juárez",
            metros_cuadrados=150,
            recamaras=3,
            banos=2,
            estacionamientos=1
        )
        
        # Verificar que se propaga la excepción
        with pytest.raises(ModeloNoDisponible):
            predict_casa(input_data)
        
        # Verificar que se llamó al método de tasa de urbanización pero no al predict
        mock_get_urban_rate.assert_called_once_with("Benito Juárez")