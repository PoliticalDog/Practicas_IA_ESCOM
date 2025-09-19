#dijstra
import numpy as np

# indice del nodo con menor costo
def obtener_nodo_minimo(lista):
    minimo_index = 0
    for i in range(1, len(lista)):
        if lista[i][0] < lista[minimo_index][0]:
            minimo_index = i
    return minimo_index

def dijkstra(maze, punto_inicial, meta):
    filas = np.shape(maze)[0]
    columnas = np.shape(maze)[1]
    distancias = np.full((filas, columnas), np.inf)
    distancias[punto_inicial] = 0

    # [(f, nodo, g, camino)]
    lista_abierta = [(0, punto_inicial, [])]
    lista_cerrada = np.zeros((filas, columnas))
    considerados = []

    while lista_abierta:
        #  nodo con el menor costo
        minimo_index = obtener_nodo_minimo(lista_abierta)
        nodo_actual_info = lista_abierta[minimo_index]

        # Desempaquetar nodo actual
        _, nodo_actual, camino_actual = nodo_actual_info
        lista_abierta[minimo_index] = lista_abierta[-1]
        lista_abierta = lista_abierta[:-1]

        x, y = nodo_actual
        considerados = considerados + [nodo_actual]

        # Si se llega al nodo meta, construir el camino
        if nodo_actual == meta:
            return camino_actual + [nodo_actual], considerados

        # Marcar nodo actual como explorado
        lista_cerrada[x, y] = 1

        # Revisar celdas vecinas
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy

            if 0 <= nx < filas and 0 <= ny < columnas and maze[nx, ny] == 0 and lista_cerrada[nx, ny] == 0:
                nuevo_costo = distancias[x, y] + (14 if abs(dx) + abs(dy) == 2 else 10)  # Coste 14 para diagonal - 10 para recto

                # hallar menor costo y actualizar
                if nuevo_costo < distancias[nx, ny]:
                    distancias[nx, ny] = nuevo_costo
                    # Agregar  nodo vecino a  lista abierta con costo actualizado
                    lista_abierta = lista_abierta + [(nuevo_costo, (nx, ny), camino_actual + [nodo_actual])]

    return None, considerados

# Movimientos  (derecha)(izquierda)(arriba)(abajo)(dia-aba-der)(dia-aba-izq)(dia-arri-der)(dia-arri-izq)
movimientos = [(0, 1), (0, -1), (-1, 0), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]