import pytest
from unittest.mock import patch, MagicMock
from domain.models import UrbanRate
from domain.exceptions import AlcaldiaNoEncontrada
from infra.services.urbanizacion import calcular_tasa


class TestServicioUrbanizacion:
    """Pruebas para el servicio de urbanización"""
    
    @patch("infra.services.urbanizacion.InegiClient")
    def test_calcular_tasa_exitoso(self, mock_inegi_client):
        """Test para verificar el cálculo exitoso de la tasa de urbanización"""
        # Configurar el mock
        mock_instance = mock_inegi_client.return_value
        mock_instance.get_poblacion_data.return_value = {
            "poblacion_total": 100000,
            "poblacion_urbana": 75000
        }
        
        # Ejecutar la función
        resultado = calcular_tasa("Benito Juárez")
        
        # Verificar el resultado
        assert isinstance(resultado, UrbanRate)
        assert resultado.alcaldia == "Benito Juárez"
        assert resultado.poblacion_total == 100000
        assert resultado.poblacion_urbana == 75000
        assert resultado.tasa_urbanizacion == 0.75
        
        # Verificar que se llamó al método correcto
        mock_instance.get_poblacion_data.assert_called_once_with("Benito Juárez")
    
    @patch("infra.services.urbanizacion.InegiClient")
    def test_calcular_tasa_alcaldia_no_encontrada(self, mock_inegi_client):
        """Test para verificar el manejo de alcaldías no encontradas"""
        # Configurar el mock para lanzar la excepción
        mock_instance = mock_inegi_client.return_value
        mock_instance.get_poblacion_data.side_effect = AlcaldiaNoEncontrada("Alcaldía Inexistente")
        
        # Verificar que se propaga la excepción
        with pytest.raises(AlcaldiaNoEncontrada):
            calcular_tasa("Alcaldía Inexistente")
            
        # Verificar que se llamó al método correcto
        mock_instance.get_poblacion_data.assert_called_once_with("Alcaldía Inexistente")
    
    @patch("infra.services.urbanizacion.InegiClient")
    def test_calcular_tasa_poblacion_cero(self, mock_inegi_client):
        """Test para verificar el manejo de población total igual a cero"""
        # Configurar el mock
        mock_instance = mock_inegi_client.return_value
        mock_instance.get_poblacion_data.return_value = {
            "poblacion_total": 0,
            "poblacion_urbana": 0
        }
        
        # Ejecutar la función
        resultado = calcular_tasa("Alcaldía Despoblada")
        
        # Verificar que no hay división por cero
        assert resultado.tasa_urbanizacion == 0.0 