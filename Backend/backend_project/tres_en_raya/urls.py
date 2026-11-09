from django.urls import path
from . import views

# Rutas de la aplicación tres en raya
urlpatterns = [
    path("", views.tres_en_raya, name="tres_en_raya"),
]