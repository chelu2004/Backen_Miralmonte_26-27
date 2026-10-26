# Importamos path para definir las rutas
from django.urls import path

# Importamos las vistas de nuestra aplicación calendario
from . import views

# Definimos el namespace de la aplicación
app_name = "calendario"

# Definimos las rutas de la aplicación
urlpatterns = [

    # Página principal del calendario con el formulario
    path("", views.inicio, name="inicio"),
      # Comprobar la fecha introducida
    path("<str:fecha>/", views.calendario, name="fecha"),

]