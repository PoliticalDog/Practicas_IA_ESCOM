#bfs
import numpy as np

def bfs(maze, punto_inicial, meta):
    cola = [(punto_inicial, [])]
    filas = np.shape(maze)[0]
    columnas = np.shape(maze)[1]
    visitados = np.zeros((filas, columnas))
    visitados[punto_inicial[0], punto_inicial[1]] = 1
    considerados = []

    while len(cola) > 0:
        nodo_actual, path = cola[0]
        cola = cola[1:]

        # Guardar los nodos que se han ido visitando
        considerados += [nodo_actual]

        if nodo_actual == meta:
            return path + [nodo_actual], considerados

        for direccion in movimientos:
            nueva_posicion = (nodo_actual[0] + direccion[0], nodo_actual[1] + direccion[1])
            # sigue dentro del laberinto
            if (0 <= nueva_posicion[0] < filas) and (0 <= nueva_posicion[1] < columnas):
                # Ver si el nodo a evaluar es accesible y no ha sido visitado
                if (maze[nueva_posicion[0], nueva_posicion[1]] == 0 and visitados[nueva_posicion[0], nueva_posicion[1]] == 0):
                    visitados[nueva_posicion[0], nueva_posicion[1]] = 1
                    cola+= [(nueva_posicion,path + [nodo_actual])]
    return None, considerados

# Lista de movimientos posibles: arriba, derecha, abajo, izquierda
movimientos = [(-1, 0), (0, 1), (1, 0), (0, -1)]