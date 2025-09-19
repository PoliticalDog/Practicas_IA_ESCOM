#DFS FINAL . revisado
import numpy as np
import matplotlib.pyplot as plt
import timeit

#INSTRUCCIONES
  #a) Realice un diagrama de flujo que ejemplifique el uso de A*
  #b) Sea la sig. matriz
  #c) Utilice el comando show() y plot para graficar el laberinto (si usa otro lenguaje se debe leer graficamente en el laberinto)
  #d) Investigue una funcion, forma o manera para que el usuario elija una coordenada y en ese punto despliegue un putno de color<<

#1 = blanco
#0 = negro

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

# DFS
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
        #considerados.append(nodo_actual)
        considerados = considerados + [nodo_actual]

        if nodo_actual == meta:
            return path + [nodo_actual], considerados

        visitados[nodo_actual[0], nodo_actual[1]] = 1
        for direccion in movimientos:
            nueva_posicion = (nodo_actual[0] + direccion[0], nodo_actual[1] + direccion[1])
            # Sigue dentro del lbaerinto
            if (0 <= nueva_posicion[0] < filas) and (0 <= nueva_posicion[1] < columnas):
                # Ver si el nodo a evaluar (nueva_posicion) es accesible y no visitado
                if maze[nueva_posicion[0], nueva_posicion[1]] == 0 and visitados[nueva_posicion[0], nueva_posicion[1]] == 0:
                    #pila.append((nueva_posicion, path + [nodo_actual]))
                    pila = pila + [(nueva_posicion, path + [nodo_actual])]
    return None, considerados

#maze --> nombre
#cmap --> colorear 0 y 1
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
            ax.plot(i[1], i[0], 'o', color='blue')
            plt.draw()      # Actualizar la grafica
            plt.pause(0.1)  # Delay para siguinete animacion

    # impresion de camino con delay
    if path:
        for j in path:
            ax.plot(j[1], j[0], 'o', color='red')
            plt.draw()      # Actualizar la grafica
            plt.pause(0.1)  # Delay para siguinete animacion

    # tiempo de ejecucion y titulo
    ax.text(len(maze[0]) / 2, -1, f"DFS - Tiempo de ejecución: {tiempo_ejecucion:.4f} ms",
            fontsize=12, color='black', ha='center', va='bottom', bbox=dict(facecolor='white', alpha=0.8))

    plt.ioff()
    plt.show()


# Ejecucion dfs
#8x15
#Varaibles globales
#punto_inicial = (4, 5)
punto_inicial = (0, 0)
#meta = (7, 14)
#meta = (7, 0)
meta = (0,12)
#Movimientos (arriba)(derecha)(abajo)(izquierda)
movimientos = [(-1, 0), (0, 1), (1, 0), (0, -1)]


inicio = timeit.default_timer()
path, considerados = dfs(matriz, punto_inicial, meta)
fin = timeit.default_timer()
tiempo_ejecucion = (fin - inicio) * 1000  # ms

# impresion
plot_maze(matriz, path, considerados, tiempo_ejecucion)