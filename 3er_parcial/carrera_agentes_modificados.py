# DFS Y BFS MODIFICADO, SE MODIFICARON LAS REGLAS DE MOVIMIENTO
# DFS: saltos de 3 casillas, incluyendo diagonales
import numpy as np
import matplotlib.pyplot as plt
import random

def generar_inicio(maze):
    while True:
        punto_inicio = (np.random.randint(0, maze.shape[0]), np.random.randint(0, maze.shape[1]))
        if maze[punto_inicio] == 0:
            return punto_inicio

# meta de 3x3
def generar_meta(maze):
    while True:
        fila = np.random.randint(0, maze.shape[0] - 2)  # -2 para evitar salir del rango
        columna = np.random.randint(0, maze.shape[1] - 2)
        if (maze[fila, columna] == 0 and maze[fila + 1, columna] == 0 and maze[fila + 2, columna] == 0 and
            maze[fila, columna + 1] == 0 and maze[fila + 1, columna + 1] == 0 and maze[fila + 2, columna + 1] == 0 and
            maze[fila, columna + 2] == 0 and maze[fila + 1, columna + 2] == 0 and maze[fila + 2, columna + 2] == 0):
            return [(fila + i, columna + j) for i in range(3) for j in range(3)], (fila + 1, columna + 1)

def esta_en_meta(nodo, meta):
    return nodo in meta

#20x20
maze = np.array([
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0],
    [0,1,0,1,1,0,1,1,1,0,1,1,1,1,1,0,0,0,1,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,1,0,0,0],
    [1,0,1,0,1,0,0,0,0,0,0,1,1,1,1,0,0,0,1,0],
    [1,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,1,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0],
    [1,0,1,0,1,0,1,0,1,1,0,1,1,0,1,0,0,1,0,1],
    [0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0],
    [1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0],
    [1,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,1,0,1],
    [0,1,0,1,0,0,0,1,0,0,0,0,0,0,1,1,1,0,1,1],
    [1,0,0,0,1,0,1,1,0,0,0,1,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0],
    [0,0,0,0,1,0,0,1,0,1,1,1,0,1,0,0,0,1,0,0],
    [1,0,1,0,0,1,0,1,1,0,0,0,1,0,0,1,0,0,0,1],
    [0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1,0,0,0,0],
    [1,0,0,0,1,0,1,1,0,0,0,1,0,1,0,1,0,0,0,0],
    [0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
    [1,0,0,0,0,1,0,0,0,0,0,0,1,0,1,1,1,0,0,0],
    [1,1,0,0,0,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0]
])

#dfs brincos de 3 casillas - diagonales
movimientos_dfs = [
    (-3, 0), (0, 3), (3, 0), (0, -3),  #  horizontales y verticales
    (-3, -3), (-3, 3), (3, -3), (3, 3)] #  diagonales

# bfs brincos de 2 casillas - sin diagonales
movimientos_bfs = [(-2, 0), (0, 2), (2, 0), (0, -2)]

# | distancia de manhattan| = |x1 - x2| + |y1 - y2|
def ordenar_movimientos(movimientos, nodo_actual, meta):
    return sorted(movimientos, key=lambda mov: min([abs(nodo_actual[0] + mov[0] - m[0]) + abs(nodo_actual[1] + mov[1] - m[1]) for m in meta]))

# bfs brincos de 2 casillas - sin diagonales
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
        considerados += [nodo_actual]

        if esta_en_meta(nodo_actual, meta):
            return path + [nodo_actual], considerados

        for direccion in movimientos_bfs:
            nueva_posicion = (nodo_actual[0] + direccion[0], nodo_actual[1] + direccion[1])
            if (0 <= nueva_posicion[0] < filas) and (0 <= nueva_posicion[1] < columnas):
                if (maze[nueva_posicion[0], nueva_posicion[1]] == 0 and visitados[nueva_posicion[0], nueva_posicion[1]] == 0):
                    visitados[nueva_posicion[0], nueva_posicion[1]] = 1
                    cola += [(nueva_posicion, path + [nodo_actual])]
    return None, considerados

# dfs brincos de 3 casillas - diagonales
def dfs(maze, punto_inicial, meta):
    pila = [(punto_inicial, [])]
    filas = np.shape(maze)[0]
    columnas = np.shape(maze)[1]
    visitados = np.zeros((filas, columnas))
    considerados = []

    while len(pila) > 0:
        nodo_actual, path = pila[-1]
        pila = pila[:-1]
        considerados = considerados + [nodo_actual]

        if esta_en_meta(nodo_actual, meta):
            return path + [nodo_actual], considerados

        visitados[nodo_actual[0], nodo_actual[1]] = 1

        # elegir moimiento ordenado cion menor costo
        movimientos_ordenados = ordenar_movimientos(movimientos_dfs, nodo_actual, meta)
        for direccion in movimientos_ordenados:
            nueva_posicion = (nodo_actual[0] + direccion[0], nodo_actual[1] + direccion[1])
            if (0 <= nueva_posicion[0] < filas) and (0 <= nueva_posicion[1] < columnas):
                if maze[nueva_posicion[0], nueva_posicion[1]] == 0 and visitados[nueva_posicion[0], nueva_posicion[1]] == 0:
                    pila = pila + [(nueva_posicion, path + [nodo_actual])]
    return None, considerados

def plot_maze(maze, bfs_considerados, dfs_considerados, start, meta, meta_centro, ganador=None):
    plt.clf()
    plt.imshow(maze, cmap='binary')
    plt.xlabel('Columnas')
    plt.ylabel('Filas')

    plt.plot(start[1], start[0], 'x', color='green', markersize=10, label="Inicio")
    plt.plot(meta_centro[1], meta_centro[0], 'x', color='purple', markersize=10, label="Meta")

    colores_path = ['red', 'blue']
    simbolos_path = ['o', 's']
    for i in range(max(len(bfs_considerados), len(dfs_considerados))):
        if i < len(bfs_considerados):
            plt.plot(bfs_considerados[i][1], bfs_considerados[i][0], simbolos_path[0], color=colores_path[0])
        if i < len(dfs_considerados):
            plt.plot(dfs_considerados[i][1], dfs_considerados[i][0], simbolos_path[1], color=colores_path[1])
        plt.pause(0.5)

    if ganador:
        plt.title(f'¡Ganador: {ganador}!', fontsize=16, color='green')
    plt.scatter([], [], color='red', marker='o', label=f'BFS saltarin 2({len(bfs_considerados)} considerados)')
    plt.scatter([], [], color='blue', marker='s', label=f'DFS saltarin 3({len(dfs_considerados)} considerados)')
    plt.legend(loc='upper right')
    plt.pause(0.5)

# EJECUCION
punto_inicio = generar_inicio(maze)
meta, meta_centro = generar_meta(maze)

bfs_path, bfs_considerados = bfs(maze, punto_inicio, meta)
dfs_path, dfs_considerados = dfs(maze, punto_inicio, meta)

# GANADOR
if bfs_considerados and dfs_considerados:
    ganador = 'BFS' if len(bfs_considerados) < len(dfs_considerados) else 'DFS'
elif bfs_considerados:
    ganador = 'BFS'
elif dfs_considerados:
    ganador = 'DFS'
else:
    ganador = 'Ninguno (Sin solucion)'

plot_maze(maze, bfs_considerados, dfs_considerados, punto_inicio, meta, meta_centro, ganador)
plt.ioff()
plt.show(block=True)
