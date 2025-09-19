# dfs y bfs, con puntos de inicio y final aleatorio
import numpy as np
import matplotlib.pyplot as plt
import random

# Generar punto de inicio aleatorio
def generar_inicio(maze):
    while True:
        punto_inicio = (np.random.randint(0, maze.shape[0]), np.random.randint(0, maze.shape[1]))
        if maze[punto_inicio] == 0:
            return punto_inicio

# Matriz dada
maze = np.array([
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
    [0,1,0,1,1,0,1,1,1,0,1,1,1,1,1],
    [0,0,0,0,0,0,0,1,1,0,0,0,0,1,0],
    [1,0,1,0,1,1,1,1,0,0,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,1,1,0,1,1,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,0,1,0,1,0,1,1,0,1,1,0,1],
    [0,0,0,0,1,0,1,0,0,0,1,1,1,0,0]
])

# Movimientos permitidos: arriba, derecha, abajo, izquierda
movimientos = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# Implementación de BFS con movimientos aleatorios
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

        if nodo_actual == meta:
            return path + [nodo_actual], considerados

        # Mezclar movimientos en cada iteración
        random.shuffle(movimientos)
        for direccion in movimientos:
            nueva_posicion = (nodo_actual[0] + direccion[0], nodo_actual[1] + direccion[1])
            if (0 <= nueva_posicion[0] < filas) and (0 <= nueva_posicion[1] < columnas):
                if (maze[nueva_posicion[0], nueva_posicion[1]] == 0 and visitados[nueva_posicion[0], nueva_posicion[1]] == 0):
                    visitados[nueva_posicion[0], nueva_posicion[1]] = 1
                    cola += [(nueva_posicion, path + [nodo_actual])]
    return None, considerados

# Implementación de DFS con movimientos aleatorios
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

        if nodo_actual == meta:
            return path + [nodo_actual], considerados

        visitados[nodo_actual[0], nodo_actual[1]] = 1

        # Mezclar movimientos en cada iteración
        random.shuffle(movimientos)
        for direccion in movimientos:
            nueva_posicion = (nodo_actual[0] + direccion[0], nodo_actual[1] + direccion[1])
            if (0 <= nueva_posicion[0] < filas) and (0 <= nueva_posicion[1] < columnas):
                if maze[nueva_posicion[0], nueva_posicion[1]] == 0 and visitados[nueva_posicion[0], nueva_posicion[1]] == 0:
                    pila = pila + [(nueva_posicion, path + [nodo_actual])]
    return None, considerados

# Visualizador del laberinto
def plot_maze(maze, bfs_considerados, dfs_considerados, start, end, ganador=None):
    plt.clf()
    plt.imshow(maze, cmap='binary')
    plt.xlabel('Columnas')
    plt.ylabel('Filas')

    # Mostrar inicio y meta
    plt.plot(start[1], start[0], 'x', color='green', markersize=10, label="Inicio")
    plt.plot(end[1], end[0], 'x', color='purple', markersize=10, label="Meta")

    # Dibujar recorridos simultáneos
    colores_path = ['red', 'blue']
    simbolos_path = ['o', 's']
    for i in range(max(len(bfs_considerados), len(dfs_considerados))):
        if i < len(bfs_considerados):
            plt.plot(bfs_considerados[i][1], bfs_considerados[i][0], simbolos_path[0], color=colores_path[0])
        if i < len(dfs_considerados):
            plt.plot(dfs_considerados[i][1], dfs_considerados[i][0], simbolos_path[1], color=colores_path[1])
        plt.pause(0.25)

    # Leyenda y ganador
    if ganador:
        plt.title(f'¡Ganador: {ganador}!', fontsize=16, color='green')
    plt.scatter([], [], color='red', marker='o', label=f'BFS ({len(bfs_considerados)} considerados)')
    plt.scatter([], [], color='blue', marker='s', label=f'DFS ({len(dfs_considerados)} considerados)')
    plt.legend(loc='upper right')
    plt.pause(0.25)

# Prueba de carrera
punto_inicio = generar_inicio(maze)
punto_final = generar_inicio(maze)

bfs_path, bfs_considerados = bfs(maze, punto_inicio, punto_final)
dfs_path, dfs_considerados = dfs(maze, punto_inicio, punto_final)

# Determinar ganador basado en nodos considerados
if bfs_considerados and dfs_considerados:
    ganador = 'BFS' if len(bfs_considerados) < len(dfs_considerados) else 'DFS'
elif bfs_considerados:
    ganador = 'BFS'
elif dfs_considerados:
    ganador = 'DFS'
else:
    ganador = 'Ninguno (Sin solución)'

plot_maze(maze, bfs_considerados, dfs_considerados, punto_inicio, punto_final, ganador)
plt.ioff()
plt.show(block=True)
