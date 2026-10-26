# Importamos path para definir las rutas
from django.urls import path

# Importamos las vistas de nuestra aplicación
from . import views

# Definimos el namespace de nuestra aplicación
app_name = "main"

# Definimos las rutas de la aplicación main
urlpatterns = [

    # Cuando entramos en /main/, ejecutamos la función main de views.py
    # name="main" permite identificar esta ruta por su nombre
   path("", views.main, name="homepage"),

]