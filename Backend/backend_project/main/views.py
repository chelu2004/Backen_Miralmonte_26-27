# Importamos render para mostrar una plantilla HTML
from django.shortcuts import render


def main(request):
    """Muestra la página principal de la aplicación main."""

    # Cargamos el HTML que está dentro de templates/main
    return render(request, "main/main.html")