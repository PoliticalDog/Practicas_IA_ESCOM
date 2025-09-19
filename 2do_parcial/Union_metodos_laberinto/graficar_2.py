#graficar 2
import matplotlib.pyplot as plt

def plot_maze_final(maze, path=None, considered=None, metodo="Método", tiempo_ejecucion=None):

    if tiempo_ejecucion is None:
        tiempo_ejecucion = 0

    plt.figure()  # Crear figura

    plt.imshow(maze, cmap='binary')
    plt.xlabel('Columnas')
    plt.ylabel('Filas')

    # Mostrar nodos considerados (visitados)
    if considered:
        for i in considered:
            plt.plot(i[1], i[0], 'o', color='blue')

    # Mostrar el camino encontrado
    if path:
        for j in path:
            plt.plot(j[1], j[0], 'o', color='red')

    plt.title(f"{metodo} - Resultados\nTiempo de ejecución: {tiempo_ejecucion:.4f} ms", fontsize=12)
    plt.show()