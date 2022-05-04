"""Tecnologias_Chapinas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # cualquier url que empiece con AnalisisRedes/ se enruta a la app de AnalisisRedes
    path('AnalisisRedes/', include('AnalisisRedes.urls'))
]

# si mandamos un request a AnalisisRedes/prueba
# django sabe que todas las peticiones que empiecen con el nombre AnalisisRedes se deben manejar por la app Analisis Redes
# AnalisisRedes/index le corta la primera parte a la url y pasa el resto al modulo de configuracion de url ---> prueba