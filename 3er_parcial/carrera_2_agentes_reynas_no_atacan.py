# 8)
# a) Realizar un programa con 2 agentes que se inicien en posiciones aleatorias en un mapa de 20x20. Que cada agente tenga dif reglas de movimiento (no pueden atravesar paredes y no se deben salir del mapa)
#    TENER UN GANADOR
# b) Resolver 1 problema a elegir mediante reglas propuestas

import numpy as np
import matplotlib.pyplot as plt

"""""""""""
# Matriz dada
maze = np.array([
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0],
    [0,1,0,1,1,0,1,1,1,0,1,1,1,1,1],
    [0,0,0,0,0,0,0,1,1,0,0,0,0,1,0],
    [1,0,1,0,1,1,1,1,0,0,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,1,1,0,1,1,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,0,1,0,1,0,1,1,0,1,1,0,1],
    [0,0,0,0,1,0,1,0,0,0,1,1,1,0,0]
])

"""""""""""
#20x35
maze = np.array([
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0],
    [0,1,0,1,1,0,1,1,1,0,1,1,1,1,1,0,0,0,1,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,1,0,0,0],
    [1,0,1,0,1,1,1,1,0,0,0,1,1,1,1,0,0,0,1,0],
    [1,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,1,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0],
    [1,1,1,0,1,0,1,0,1,1,0,1,1,0,1,0,0,1,0,1],
    [0,1,0,1,1,0,1,0,0,0,1,1,1,0,0,1,0,0,0,0],
    [1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0],
    [1,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,1,0,1],
    [0,1,0,1,1,0,0,1,0,0,0,0,0,0,1,1,1,0,1,1],
    [1,0,0,0,1,0,1,1,0,0,0,1,0,0,0,0,0,1,0,0],
    [0,1,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0],
    [0,0,0,0,1,0,0,1,0,1,1,1,0,1,0,0,0,1,0,0],
    [1,0,1,0,0,1,0,1,1,0,0,0,1,0,0,1,0,0,0,1],
    [0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1,0,0,0,0],
    [1,0,0,0,1,0,1,1,0,0,0,1,0,1,0,1,0,0,0,0],
    [0,1,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0],
    [1,1,0,0,1,1,0,0,1,1,1,0,1,0,1,1,1,0,0,0],
    [1,1,1,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0]
])

def generar_inicio(maze):
    while True:
        punto_inicio = (np.random.randint(0, maze.shape[0]), np.random.randint(0, maze.shape[1]))
        if maze[punto_inicio] == 0:
            return punto_inicio

def generar_reinas(maze, cantidad):
    libres = [(i, j) for i in range(maze.shape[0]) for j in range(maze.shape[1]) if maze[i, j] == 0]
    if cantidad > len(libres):
        print("No hay muchos espacios libres para generar las reynas")
        exit()
    np.random.shuffle(libres)
    reinas = libres[:cantidad]
    return reinas

# Movimientos permitidos: arriba, derecha, abajo, izquierda
movimientos = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(maze, punto_inicial, reinas):
    cola = [(punto_inicial, [])]
    filas, columnas = maze.shape
    visitados = np.zeros((filas, columnas))
    visitados[punto_inicial[0], punto_inicial[1]] = 1
    considerados = []
    reinas_consumidas = []

    while len(cola) > 0 and len(reinas_consumidas) < len(reinas):
        nodo_actual, path = cola[0]
        cola = cola[1:]
        considerados += [nodo_actual]

        if nodo_actual in reinas and nodo_actual not in reinas_consumidas:
            reinas_consumidas = reinas_consumidas + [nodo_actual]

        for direccion in movimientos:
            nueva_posicion = (nodo_actual[0] + direccion[0], nodo_actual[1] + direccion[1])
            if (0 <= nueva_posicion[0] < filas) and (0 <= nueva_posicion[1] < columnas):
                if (maze[nueva_posicion[0], nueva_posicion[1]] == 0 and visitados[nueva_posicion[0], nueva_posicion[1]] == 0):
                    visitados[nueva_posicion[0], nueva_posicion[1]] = 1
                    cola = cola + [(nueva_posicion, path + [nodo_actual])]
    return considerados, len(reinas_consumidas)

def dfs(maze, punto_inicial, reinas):
    pila = [(punto_inicial, [])]
    filas, columnas = maze.shape
    visitados = np.zeros((filas, columnas))
    considerados = []
    reinas_consumidas = []

    while len(pila) > 0 and len(reinas_consumidas) < len(reinas):
        nodo_actual, path = pila[-1]
        pila = pila[:-1]
        considerados = considerados + [nodo_actual]

        if nodo_actual in reinas and nodo_actual not in reinas_consumidas:
            reinas_consumidas = reinas_consumidas + [nodo_actual]

        visitados[nodo_actual[0], nodo_actual[1]] = 1
        for direccion in movimientos:
            nueva_posicion = (nodo_actual[0] + direccion[0], nodo_actual[1] + direccion[1])
            if (0 <= nueva_posicion[0] < filas) and (0 <= nueva_posicion[1] < columnas):
                if maze[nueva_posicion[0], nueva_posicion[1]] == 0 and visitados[nueva_posicion[0], nueva_posicion[1]] == 0:
                    pila = pila + [(nueva_posicion, path + [nodo_actual])]
    return considerados, len(reinas_consumidas)

def plot_maze(maze, bfs_path, dfs_path, start, reinas, bfs_movimientos, dfs_movimientos, ganador):
    plt.clf()
    cmap = plt.get_cmap('binary')
    plt.imshow(maze, cmap=cmap)
    plt.xlabel('Columnas')
    plt.ylabel('Filas')

    #plt.legend(['Inicio', 'Reinas', 'BFS (o, rojo)', 'DFS (s, azul)'], loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4)
    plt.legend(
        [
            plt.Line2D([0], [0], marker='x', color='green', markersize=10, linestyle='None'),
            plt.Line2D([0], [0], marker='P', color='purple', markersize=10, linestyle='None'),
            plt.Line2D([0], [0], marker='o', color='red', markersize=10, linestyle='None'),
            plt.Line2D([0], [0], marker='s', color='blue', markersize=10, linestyle='None'),
        ],
        ['Inicio', 'Reinas', 'BFS (o, rojo)', 'DFS (s, azul)'],
        loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4, frameon=True
    )


    plt.plot(start[1], start[0], 'x', color='purple', markersize=10)
    for reina in reinas:
        plt.plot(reina[1], reina[0], 'P', color='purple', markersize=10)

    colores_path = ['red', 'blue']
    simbolos_path = ['o', 's']

    for i in range(max(len(bfs_path), len(dfs_path))):
        if i < len(bfs_path):
            plt.plot(bfs_path[i][1], bfs_path[i][0], simbolos_path[0], color=colores_path[0])
        if i < len(dfs_path):
            plt.plot(dfs_path[i][1], dfs_path[i][0], simbolos_path[1], color=colores_path[1])
        plt.pause(0.1)

    plt.title(f'Ganador: {ganador}\nMovimientos BFS: {bfs_movimientos}, DFS: {dfs_movimientos}', fontsize=16, color='green', pad=10)
    plt.pause(1)

#cantidad=5
cantidad = int(input("Numero de reynas: "))
punto_inicio = generar_inicio(maze)
reinas = generar_reinas(maze, cantidad)

bfs_path, bfs_reinas = bfs(maze, punto_inicio, reinas)
dfs_path, dfs_reinas = dfs(maze, punto_inicio, reinas)

if bfs_reinas == len(reinas) and dfs_reinas == len(reinas):
    ganador = 'BFS' if len(bfs_path) < len(dfs_path) else 'DFS'
elif bfs_reinas == len(reinas):
    ganador = 'BFS'
elif dfs_reinas == len(reinas):
    ganador = 'DFS'
else:
    ganador = 'Ninguno gano'

plot_maze(maze, bfs_path, dfs_path, punto_inicio, reinas, len(bfs_path), len(dfs_path), ganador)

plt.ioff()
plt.show(block=True)
