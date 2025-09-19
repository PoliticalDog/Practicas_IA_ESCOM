#dfs
import numpy as np

def dfs(maze, punto_inicial, meta):
    pila = [(punto_inicial, [])]
    filas = np.shape(maze)[0]
    columnas = np.shape(maze)[1]
    visitados = np.zeros((filas, columnas))
    considerados = []

    while len(pila) > 0:
        nodo_actual, path = pila[-1]
        pila = pila[:-1]

        # nodos visitados
        considerados = considerados + [nodo_actual]

        if nodo_actual == meta:
            return path + [nodo_actual], considerados

        visitados[nodo_actual[0], nodo_actual[1]] = 1
        for direccion in movimientos:
            nueva_posicion = (nodo_actual[0] + direccion[0], nodo_actual[1] + direccion[1])
            # Sigue dentro del laberinto
            if (0 <= nueva_posicion[0] < filas) and (0 <= nueva_posicion[1] < columnas):
                # Ver si el nodo a evaluar (nueva_posicion) es accesible y no visitado
                if maze[nueva_posicion[0], nueva_posicion[1]] == 0 and visitados[nueva_posicion[0], nueva_posicion[1]] == 0:
                    pila = pila + [(nueva_posicion, path + [nodo_actual])]

    return None, considerados

# Movimientos permitidos: arriba, derecha, abajo, izquierda
movimientos = [(-1, 0), (0, 1), (1, 0), (0, -1)]