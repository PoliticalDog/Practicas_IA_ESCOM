#main
import numpy as np
import matplotlib.pyplot as plt
import timeit
from bfs import bfs
from dfs import dfs
from a_estrella import a_estrella
from disjktra import dijkstra
from graficar import plot_maze
from graficar_2 import plot_maze_final


"""""""""
# Matriz del laberinto
maze = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0]
])

"""""""""
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

def mostrar_tiempos(tiempos):
    metodos = ['BFS', 'DFS', 'A*', 'Dijkstra']
    plt.bar(metodos, tiempos, color=['blue', 'green', 'red', 'purple'])
    plt.xlabel('Métodos')
    plt.ylabel('Tiempo de ejecución (ms)')
    plt.title('Comparación de tiempos de ejecución de los métodos')
    plt.show()

def main():
    print("Seleccione el método para resolver el laberinto:")
    print("1. BFS")
    print("2. DFS")
    print("3. A*")
    print("4. Dijkstra")
    metodo = int(input("Ingresa el número del método: "))

    # Pedir punto inicial y meta
    #punto_inicial = (1, 1)
    #meta = (19,28)
    punto_inicial = tuple(map(int, input("Punto inicial (x,y), ingresar #,#: ").split(',')))
    meta = tuple(map(int, input("Punto meta (x,y), ingresar #,#: ").split(',')))

    # validacion de punto dentro y libre
    def es_valido(maze, punto):
        filas, columnas = maze.shape
        x, y = punto
        return 0 <= x < filas and 0 <= y < columnas and maze[x][y] == 0

    if not es_valido(maze, punto_inicial):
        print("El punto inicial no es válido (fuera del laberinto o bloqueado).")
        return

    if not es_valido(maze, meta):
        print("El punto meta no es válido (fuera del laberinto o bloqueado).")
        return

    # EJECUCION SEGUN SELECCION
    inicio = timeit.default_timer()
    if metodo == 1:
        path, considerados = bfs(maze, punto_inicial, meta)
        metodo_nombre = "BFS"
    elif metodo == 2:
        path, considerados = dfs(maze, punto_inicial, meta)
        metodo_nombre = "DFS"
    elif metodo == 3:
        path, considerados = a_estrella(maze, punto_inicial, meta)
        metodo_nombre = "A*"
    elif metodo == 4:
        path, considerados = dijkstra(maze, punto_inicial, meta)
        metodo_nombre = "Dijkstra"
    else:
        print("Ingresa un metodo valido.")
        return
    fin = timeit.default_timer()

    # Mostrar los resultados
    tiempo_ejecucion = (fin - inicio) * 1000  # Convertir a milisegundos
    plot_maze(maze, path, considerados, tiempo_ejecucion, metodo=metodo_nombre)

    # Preguntar si el usuario quiere ejecutar los 4 métodos
    ejecutar_todos = input("Quieres ejecutar los 4 métodos? (BFS, DFS, A*, Dijkstra)? (s/n): ").strip().lower()

    if ejecutar_todos == 's':
        # todos los metodos
        inicio_bfs = timeit.default_timer()
        path_bfs, considerados_bfs = bfs(maze, punto_inicial, meta)
        fin_bfs = timeit.default_timer()
        print ("Termino bfs")

        inicio_dfs = timeit.default_timer()
        path_dfs, considerados_dfs = dfs(maze, punto_inicial, meta)
        fin_dfs = timeit.default_timer()
        print ("Termino dfs")

        inicio_dijkstra = timeit.default_timer()
        path_dijkstra, considerados_dijkstra = dijkstra(maze, punto_inicial, meta)
        fin_dijkstra = timeit.default_timer()
        print ("Termino dijkstra")

        inicio_a_star = timeit.default_timer()
        path_a_estrella, considerados_a_estrella = a_estrella(maze, punto_inicial, meta)
        fin_a_star = timeit.default_timer()
        print ("Termino A*")

        # tiempos
        tiempo_bfs = (fin_bfs - inicio_bfs) * 1000
        tiempo_dfs = (fin_dfs - inicio_dfs) * 1000
        tiempo_a_star = (fin_a_star - inicio_a_star) * 1000
        tiempo_dijkstra = (fin_dijkstra - inicio_dijkstra) * 1000

        # Figuras de cada metodo
        plot_maze_final(maze, path_bfs, considerados_bfs, metodo="BFS", tiempo_ejecucion=tiempo_bfs)
        plot_maze_final(maze, path_dfs, considerados_dfs, metodo="DFS", tiempo_ejecucion=tiempo_dfs)
        plot_maze_final(maze, path_a_estrella, considerados_a_estrella, metodo="A*", tiempo_ejecucion=tiempo_a_star)
        plot_maze_final(maze, path_dijkstra, considerados_dijkstra, metodo="Dijkstra", tiempo_ejecucion=tiempo_dijkstra)

        # Comparativa final de cada metodo
        mostrar_tiempos([tiempo_bfs, tiempo_dfs, tiempo_a_star, tiempo_dijkstra])

if __name__ == "__main__":
    main()