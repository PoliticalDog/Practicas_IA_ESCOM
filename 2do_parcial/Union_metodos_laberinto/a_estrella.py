#a_estrella
import numpy as np

# h Manhattan
def heuristica(nodo, meta):
    return abs(nodo[0] - meta[0]) + abs(nodo[1] - meta[1])

"""""""""
# h euclidiana
def heuristica(nodo, meta):
    return ((nodo[0] - meta[0])**2 + (nodo[1] - meta[1])**2)**0.5

    """""""""

# indice menor f = costo total
def obtener_nodo_minimo(lista):
    minimo_index = 0
    for i in range(1, len(lista)):
        if lista[i][0] < lista[minimo_index][0]:
            minimo_index = i
    return minimo_index

def a_estrella(maze, punto_inicial, meta):
    # [(f, nodo, g, camino)]
    lista_abierta = [(0, punto_inicial, 0, [])]
    filas = np.shape(maze)[0]
    columnas = np.shape(maze)[1]
    lista_cerrada = np.zeros((filas, columnas))
    considerados = []

    while lista_abierta:
        # indice del menor f
        minimo_index = obtener_nodo_minimo(lista_abierta)
        nodo_actual_info = lista_abierta[minimo_index]

        # desempaquetar nodo actual
        _, nodo_actual, costo_g, camino_actual = nodo_actual_info
        lista_abierta[minimo_index] = lista_abierta[-1]
        lista_abierta = lista_abierta[:-1]  # pase de valor a la ultima posicion y elimnacion
        considerados = considerados + [nodo_actual]
        if nodo_actual == meta:
            return camino_actual + [nodo_actual], considerados

        lista_cerrada[nodo_actual[0], nodo_actual[1]] = 1

        # Exploracion de vecinos
        for direccion in movimientos:
            nueva_posicion = (nodo_actual[0] + direccion[0], nodo_actual[1] + direccion[1])
            if 0 <= nueva_posicion[0] < filas and 0 <= nueva_posicion[1] < columnas:
                if maze[nueva_posicion[0], nueva_posicion[1]] == 0 and lista_cerrada[nueva_posicion[0], nueva_posicion[1]] == 0:
                    # g segun la direccion
                    if abs(direccion[0]) + abs(direccion[1]) == 2:  #diagonal
                        g_nuevo = costo_g + 14  #diagonal
                    else:  # Movimiento recto (horizontal o vertical)
                        g_nuevo = costo_g + 10  # recto

                    f_nuevo = g_nuevo + heuristica(nueva_posicion, meta)

                    # no esta en la lista abierta se añade
                    if nueva_posicion not in [n[1] for n in lista_abierta]:
                        lista_abierta = lista_abierta + [(f_nuevo, nueva_posicion, g_nuevo, camino_actual + [nodo_actual])]
                        considerados = considerados + [nueva_posicion]

    return None, considerados

# Movimientos  (derecha)(izquierda)(arriba)(abajo)(dia-aba-der)(dia-aba-izq)(dia-arri-der)(dia-arri-izq)
movimientos = [(0, 1), (0, -1), (-1, 0), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]