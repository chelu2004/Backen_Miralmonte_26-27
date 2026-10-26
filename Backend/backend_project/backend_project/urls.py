"""
URL configuration for backend_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
# Importamos el panel de administración de Django
from django.contrib import admin

# Importamos path para definir rutas e include para incluir otras aplicaciones
from django.urls import path, include

# Importamos las vistas de nuestro proyecto
from . import views


# Definimos las rutas principales del proyecto
urlpatterns = [

    # Ruta del panel de administración
    path("admin/", admin.site.urls),

    # Ruta de la página principal
    path("", views.homepage, name="homepage"),

    # Ruta de nuestra aplicación main
    path("main/", include("main.urls")),

    # Ruta de la página de contacto
    path("contacto/", views.contacto, name="contacto"),

      # Rutas de nuestra nueva aplicación calendario
    path("calendario/", include("calendario.urls")),

]