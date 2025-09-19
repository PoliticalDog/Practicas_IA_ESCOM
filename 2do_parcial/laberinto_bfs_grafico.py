#BFS FINAL . revisado
import numpy as np
import matplotlib.pyplot as plt
import timeit

#8x15
matriz = np.array([
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
    [0,1,0,1,1,0,1,1,1,0,1,1,1,1,1],
    [0,0,0,0,0,0,0,1,1,0,0,0,0,1,0],
    [1,0,1,0,1,1,1,1,0,0,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,1,1,0,1,1,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,0,1,0,1,0,1,1,0,1,1,0,1],
    [0,0,0,0,1,0,1,0,0,0,1,1,1,0,0]
])

# BFS
def bfs(maze, punto_inicial, meta):
    cola = [(punto_inicial, [])]
    filas = np.shape(maze)[0]
    columnas = np.shape(maze)[1]
    visitados = np.zeros((filas, columnas))
    considerados = []

    while len(cola) > 0:
        nodo_actual, path = cola[0]
        cola = cola[1:]

        # nodos visitados
        #considerados.append(nodo_actual)
        considerados = considerados + [nodo_actual]

        if nodo_actual == meta:
            return path + [nodo_actual], considerados

        visitados[nodo_actual[0], nodo_actual[1]] = 1
        for direccion in movimientos:
            nueva_posicion = (nodo_actual[0] + direccion[0], nodo_actual[1] + direccion[1])
            # sigue dentro del laberinto
            if (0 <= nueva_posicion[0] < filas) and (0 <= nueva_posicion[1] < columnas):
                # ver si el nodo a evaluar (nueva_posicion) es accesible y no visitado
                if maze[nueva_posicion[0], nueva_posicion[1]] == 0 and visitados[nueva_posicion[0], nueva_posicion[1]] == 0:
                    #cola.append((nueva_posicion, path + [nodo_actual]))
                    cola = cola + [(nueva_posicion, path + [nodo_actual])]
    return None, considerados

# impresion de laberinto
def plot_maze(maze, path=None, considered=None, tiempo_ejecucion=None):
    plt.ion()  # modo dinamico

    fig, ax = plt.subplots()
    ax.imshow(maze, cmap='binary')
    ax.set_xlabel('Columnas')
    ax.set_ylabel('Filas')


    # impresion de visitados con delay
    if considered:
        for i in considered:
            plt.plot(i[1], i[0], 'o', color='blue')
            plt.draw()      # Actualizar la grafica
            plt.pause(0.1)  # Delay para siguinete animacion
    # impresion de camino con delay
    if path:
        for j in path:
            plt.plot(j[1], j[0], 'o', color='red')

    # tiempo de ejecucion y titulo
    ax.text(len(maze[0]) / 2, -1, f"BFS - Tiempo de ejecución: {tiempo_ejecucion:.4f} ms",
            fontsize=12, color='black', ha='center', va='bottom', bbox=dict(facecolor='white', alpha=0.8))

    plt.ioff()  # Desactivar el modo dinamico
    plt.show()  # Muestra la animcaion


# Variables globales
#8x15
punto_inicial = (0, 1)
meta = (7, 14)
# Movimientos (arriba)(derecha)(abajo)(izquierda)
movimientos = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#tiempo
inicio = timeit.default_timer()
path, considerados = bfs(matriz, punto_inicial, meta)
fin = timeit.default_timer()
tiempo_ejecucion = (fin - inicio) * 1000

# impresion partes graficas
plot_maze(matriz, path, considerados, tiempo_ejecucion)