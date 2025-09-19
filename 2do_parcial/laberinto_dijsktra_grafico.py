#final final
import numpy as np
import matplotlib.pyplot as plt
import timeit

"""""""""
#20x35
#20 filas y 35 columnas
maze = np.array([
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1],
    [0,1,0,1,1,0,1,1,1,0,1,1,1,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,0,1,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1],
    [1,0,1,0,1,1,1,1,0,0,0,1,1,1,1,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,0,0],
    [1,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0],
    [1,1,1,0,1,0,1,0,1,1,0,1,1,0,1,0,0,1,0,0,1,0,1,0,1,0,1,1,1,0,0,0,0,0,1],
    [0,1,0,1,1,0,1,0,0,0,1,1,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,1,1,0,1,0,0],
    [1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,1,0,1,0],
    [1,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0],
    [0,1,0,1,1,0,0,1,0,0,0,0,0,0,1,0,1,1,0,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1],
    [1,0,0,0,1,0,1,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0],
    [0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0],
    [0,0,0,0,1,0,0,1,0,1,1,1,0,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,0,1,0,1,1,0,1],
    [1,0,1,0,0,1,0,1,1,0,0,0,0,1,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,1,1,0,0,1,0],
    [0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0,1,0,1,1,0,1,1,0,1,0,0,1,0,0],
    [1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1],
    [0,1,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0],
    [1,1,0,0,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,1,0],
    [1,1,1,0,1,0,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0]
])
"""""""""
#8x15
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
                nuevo_costo = distancias[x, y] + (14 if abs(dx) + abs(dy) == 2 else 10)  # coste 14 para diagonal - 10 para recto

                # hallar menor costo y actualizar
                if nuevo_costo < distancias[nx, ny]:
                    distancias[nx, ny] = nuevo_costo
                    # Agregar  nodo vecino a  lista abierta con costo actualizado
                    lista_abierta = lista_abierta + [(nuevo_costo, (nx, ny), camino_actual + [nodo_actual])]

    return None, considerados

def plot_maze(maze, path=None, considerados=None, tiempo_ejecucion=None):
    plt.ion()
    fig, ax = plt.subplots()
    ax.imshow(maze, cmap='binary')
    ax.set_xlabel('Columnas')
    ax.set_ylabel('Filas')

    if considerados:
        for i in considerados:
            ax.plot(i[1], i[0], 'o', color='blue')
            plt.draw()  # Actualizar
            plt.pause(0.1)

    if path:
        for j in path:
            ax.plot(j[1], j[0], 'o', color='red')
            plt.draw()  # Actualizar
            plt.pause(0.1)

    ax.text(len(maze[0]) / 2, -1, f"Dijkstra - Tiempo de ejecución: {tiempo_ejecucion:.4f} ms",
            fontsize=12, color='black', ha='center', va='bottom', bbox=dict(facecolor='white', alpha=1))

    plt.ioff()
    plt.show()


# Movimientos  (derecha)(izquierda)(arriba)(abajo)(dia-aba-der)(dia-aba-izq)(dia-arri-der)(dia-arri-izq)
movimientos = [(0, 1), (0, -1), (-1, 0), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
punto_inicial = (2, 0)
#meta = (19, 34)
meta = (7, 14)

# tiempo
inicio = timeit.default_timer()
path, considerados = dijkstra(maze, punto_inicial, meta)
fin = timeit.default_timer()
tiempo_ejecucion = (fin - inicio) * 1000  # Convertir a milisegundos

plot_maze(maze, path, considerados, tiempo_ejecucion)