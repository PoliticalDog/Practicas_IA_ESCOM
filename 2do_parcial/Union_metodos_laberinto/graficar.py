#graficar 1
import matplotlib.pyplot as plt

def plot_maze(maze, path=None, considered=None, tiempo_ejecucion=None, metodo="Método"):
    plt.ion()  # Modo dinámico para la animación

    fig, ax = plt.subplots()
    ax.imshow(maze, cmap='binary')
    ax.set_xlabel('Columnas')
    ax.set_ylabel('Filas')

    if considered:
        for i in considered:
            plt.plot(i[1], i[0], 'o', color='blue', label="Nodos Visitados")
            plt.draw()
            plt.pause(0.1)

    if path:
        for j in path:
            plt.plot(j[1], j[0], 'o', color='red', label="Camino Encontrado")
            plt.draw()
            plt.pause(0.1)

    ax.text(len(maze[0]) / 2, -3, f"{metodo} - Tiempo de ejecución: {tiempo_ejecucion:.4f} ms",
        fontsize=12, color='black', ha='center', va='bottom', bbox=dict(facecolor='white', alpha=0.8))

    ax.set_title(f"Laberinto Resuelto con {metodo}")
    print("Presiona cualquier tecla para continuar ")
    plt.waitforbuttonpress()

    #plt.clf()

    plt.ioff()
    plt.show()
