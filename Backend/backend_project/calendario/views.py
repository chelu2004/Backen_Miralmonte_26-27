# Importamos render para mostrar plantillas HTML
from django.shortcuts import render

# Importamos datetime para trabajar con fechas
from datetime import datetime

# Vista que muestra el formulario del calendario
def inicio(request):
    return render(request, "calendario/inicio.html")

def calendario(request, fecha):
    """Recibe una fecha y muestra su información."""

    try:
        # Convertimos el texto recibido en una fecha real
        # El formato debe ser DD-MM-AAAA
        fecha_convertida = datetime.strptime(fecha, "%d-%m-%Y")

        # Obtenemos el día, mes y año
        mi_dia = fecha_convertida.day
        mi_mes = fecha_convertida.month
        mi_ano = fecha_convertida.year

        # Creamos un mensaje para mostrar en el HTML
        mensaje = "La fecha introducida es correcta"

        # Enviamos los datos a nuestra plantilla HTML
        return render(request, "calendario/fecha.html", {
            "dia": mi_dia,
            "mes": mi_mes,
            "ano": mi_ano,
            "mensaje": mensaje
        })

    except ValueError:
        # Si la fecha es incorrecta, mostramos una página de error
        return render(request, "calendario/error.html", {
            "mensaje": "La fecha introducida no es válida. Utiliza DD-MM-AAAA."
        }, status=400)