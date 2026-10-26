# Importamos render para mostrar plantillas HTML
from django.shortcuts import render


def homepage(request):
    """Muestra la página principal del proyecto."""

    # Cargamos el archivo home.html
    return render(request, "home.html")


def contacto(request):
    """Muestra la página de contacto."""

    # Cargamos el archivo contacto.html
    return render(request, "contacto.html")