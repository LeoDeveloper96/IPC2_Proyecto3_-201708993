from Modelos.Mensaje import Mensaje
from Modelos.Empresa import empresa
from Modelos.Servicio import servicio
from Modelos.Solicitud import solicitud

class manager:

    def __init__(self):
        self.solicitudes = []

    def agregar_solicitud(self, mensajes, negativos, positivos, empresas):
        self.solicitudes.append(solicitud(mensajes, negativos, positivos, empresas))

    def obtener_solicitudes(self):
        json = []
        for solicitud in self.solicitudes:
            solicitud = {
                'mensajes': solicitud.mensajes,
                'negativos': solicitud.negativos,
                'positivos': solicitud.positivos,
                'empresas': solicitud.empresas
            }
            json.append(solicitud)
        return json

def crearArchivoAlmacenamiento(self):
    pass


def resumenporFecha(self, fecha, empresa, empresas):
    pass


def resumenporRangoFecha(self, fecha1, fecha2, empresa, empresas):
    pass