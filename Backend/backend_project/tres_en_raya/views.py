from django.shortcuts import render


# Vista del juego tres en raya
def tres_en_raya(request):

    # Creamos el tablero inicial
    tablero = ['-'] * 9
    turno = 'X'
    mensaje = 'Turno de X'
    terminado = False

    # Combinaciones para ganar
    combinaciones = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    # Si el jugador pulsa una casilla
    if request.method == 'POST':

        # Recuperamos los datos del formulario
        tablero = list(request.POST.get('tablero', '---------'))
        turno = request.POST.get('turno', 'X')
        posicion = request.POST.get('posicion')

        # Comprobamos los datos recibidos
        if len(tablero) != 9 or any(c not in ['X', 'O', '-'] for c in tablero):
            tablero = ['-'] * 9
            turno = 'X'

        if turno not in ['X', 'O']:
            turno = 'X'

        # Comprobamos que la partida no estuviera terminada
        partida_acabada = '-' not in tablero

        for a, b, c in combinaciones:
            if tablero[a] != '-' and tablero[a] == tablero[b] == tablero[c]:
                partida_acabada = True

        # Colocamos la ficha si la casilla está vacía
        if not partida_acabada and posicion is not None and posicion.isdigit():
            posicion = int(posicion)

            if 0 <= posicion < 9 and tablero[posicion] == '-':
                tablero[posicion] = turno

                # Cambiamos el turno
                if turno == 'X':
                    turno = 'O'
                else:
                    turno = 'X'

    # Comprobamos si alguien ha ganado
    for a, b, c in combinaciones:
        if tablero[a] != '-' and tablero[a] == tablero[b] == tablero[c]:
            mensaje = '¡Ha ganado ' + tablero[a] + '!'
            terminado = True
            break

    # Comprobamos si hay empate
    if not terminado and '-' not in tablero:
        mensaje = '¡Empate!'
        terminado = True

    # Si la partida continúa
    if not terminado:
        mensaje = 'Turno de ' + turno

    # Enviamos los datos al HTML
    contexto = {
        'tablero': tablero,
        'turno': turno,
        'mensaje': mensaje,
        'terminado': terminado,
    }

    return render(request, 'tres_en_raya.html', contexto)