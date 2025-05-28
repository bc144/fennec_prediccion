class DomainException(Exception):
    """Excepción base para errores de dominio"""
    pass


class AlcaldiaNoEncontrada(DomainException):
    """Se levanta cuando no se encuentra información de una alcaldía"""
    def __init__(self, alcaldia: str):
        self.alcaldia = alcaldia
        super().__init__(f"No se encontró información para la alcaldía: {alcaldia}")


class ModeloNoDisponible(DomainException):
    """Se levanta cuando no se puede cargar un modelo predictivo"""
    def __init__(self, tipo_modelo: str):
        self.tipo_modelo = tipo_modelo
        super().__init__(f"No se pudo cargar el modelo predictivo: {tipo_modelo}")


class FeatureNoValida(DomainException):
    """Se levanta cuando una característica no es válida para el modelo"""
    def __init__(self, feature: str, valor):
        self.feature = feature
        self.valor = valor
        super().__init__(f"La característica '{feature}' con valor '{valor}' no es válida para el modelo")


class ErrorPrediccion(DomainException):
    """Se levanta cuando hay un error en la predicción"""
    def __init__(self, mensaje: str):
        super().__init__(f"Error en la predicción: {mensaje}")


class ErrorEstadisticas(DomainException):
    """Se lanza cuando hay un error al calcular estadísticas"""
    pass


class FibraNoEncontrada(DomainException):
    """Se lanza cuando no se encuentra información para una FIBRA"""
    pass


class ErrorFibras(DomainException):
    """Se lanza cuando hay un error al procesar datos de FIBRAs"""
    def __init__(self, mensaje: str):
        super().__init__(f"Error al procesar FIBRAs: {mensaje}") 