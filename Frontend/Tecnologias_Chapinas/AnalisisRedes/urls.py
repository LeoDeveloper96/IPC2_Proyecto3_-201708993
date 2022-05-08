# en este modulo mapeo mi urls a mis views

from django.urls import path
# para poder referenciar mi funcion views
from . import views

#URL CONF, cada app puede tener su propio modulo de configuracion
# Se debe importar esta configuracion a la configuracion principal de este proyecto, o sea dentro de Tecnologias chapinas en urls
# este nombre debe estar escrito asi
urlpatterns = [
    # aqui le doy un path o una url y una funcion de views
    # como el metodo no tiene parentesis significa que solo paso una refencia a la funcion
    # aqui solo paso index porque ya verifique que viniera AnalisisRedes/... en mi modulo de configuracion principal
    # las rutas siempre terminan con /
    path('', views.index),
    path('/enviar', views.enviar)
]