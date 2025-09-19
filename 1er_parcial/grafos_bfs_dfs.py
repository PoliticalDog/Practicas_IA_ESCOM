import tracemalloc as mem
import time as tm
import random as ran

"""
Practica 1
1) Ingresar cualquier grafo
2) Generar un número aleatorio entero dentro del rango del numero de nodos
3) Para BFS Y DFS cuando encuentre la bandera se detenga el programa
4) Medir tiempo y memoria (compare ambos algoritmos)
"""

tiempo_dfs = None
tiempo_bfs = None
memoria_dfs = None
memoria_bfs = None

#def = funcion
def dfs(grafo, nodo_raiz, bandera):
    global tiempo_dfs, memoria_dfs       #globales para comparacion
    #cronometro y memoria
    start_time = tm.time_ns()
    mem.start()

    #inicio de variables
    previo = [None] * len(grafo)  # lista "dinamica"
    tope = 0                      # indice de mi pila
    previo[tope] = nodo_raiz
    visitados = [False] * (len(grafo) + 1)  #arreglo visitados
    visitados[nodo_raiz] = True             #false

    #i = 0 #indice mi pila de previos
    #while i < len(previo) and  bandera_encontrada_dfs==False:
    #while previo:
    while tope >= 0:
        #nodo_actual, *previo = previo
        #nodo_actual = previo.pop() #Eliminar pop por algo mas
        nodo_actual = previo[tope]  # Obtener el nodo actual
        tope = tope - 1             # pop() casero

        if nodo_actual == nodo_raiz:
            print(f"Raiz {nodo_actual}")
            print("  |")
        elif nodo_actual == bandera:
            print(f"Se llego al nodo '{nodo_actual}' destino con DFS")
            break
        else:
            print(f"  {nodo_actual}")
            print("  |")

        #recorremos nodos hijos  --> Reversded para inverit el sentido horario
        for vecino in reversed(grafo[nodo_actual]):
            if not visitados[vecino]:
                visitados[vecino] = True
                #previo.append(vecino)
                tope = tope + 1         #  append()
                previo[tope] = vecino
                #previo.append(vecino) #Eliminar append, es nativo de python
        #i = i + 1

    end = tm.time_ns()
    tiempo_dfs = end - start_time
    print(f"Tiempo de ejecucion: {tiempo_dfs} nanosegundos")    #tiempo
    current, peak = mem.get_traced_memory()                     # memoria
    mem.stop()
    memoria_dfs = current
    print(f"Memoria de ejecucion: {memoria_dfs} KB")

def bfs(grafo, nodo_raiz, bandera):
    global tiempo_bfs, memoria_bfs
    #Cronometro y memoria
    start_time = tm.time_ns()
    mem.start()

    #inicio de variables
    previo = [None] * len(grafo)
    inicio = 0
    final = 0
    previo[final] = nodo_raiz
    final += 1
    visitados = [False] * (len(grafo) + 1)
    visitados[nodo_raiz] = True

    #while i < len(previo):
    while inicio < final:
        #nodo_actual = previo.pop(0)          # cambiar pop por otra fuuncion
        nodo_actual = previo[inicio]          # Obtener el nodo actual
        inicio = inicio + 1                   # simula el pop(0)

        if nodo_actual == nodo_raiz:
            print(f"Raiz {nodo_actual}")
            print("  |")
        elif nodo_actual == bandera:
            print(f"Se llego al nodo '{nodo_actual}' destino con BFS")
            break
        else:
            print(f"  {nodo_actual}")
            print("  |")

        # recorremos nodos hermanos
        for vecino in grafo[nodo_actual]:
            if not visitados[vecino]:
                visitados[vecino] = True
                previo[final] = vecino  # Coloca el vecino al final
                final = final + 1  # simula append

    end = tm.time_ns()
    tiempo_bfs = end - start_time
    print(f"Tiempo de ejecucion: {tiempo_bfs} nanosegundos")
    current, peak = mem.get_traced_memory()
    mem.stop()
    memoria_bfs = current
    print(f"Memoria utilizada: {memoria_bfs} KB")

# Definimos el grafo
grafo = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6, 7],
    4: [2],
    5: [2, 8],
    6: [3],
    7: [3],
    8: [5]
}

#parametros
raiz = 1
print(f"\nEl nodo raiz es: {raiz} ")
bandera = ran.randint(1,8)
if bandera == raiz:
    bandera = ran.randint(1,8)
print(f"El nodo bandera generado aleatorio fue: {bandera} ")


#EJECUCION DFS Y BFS
print("\n  DFS")
dfs(grafo, raiz, bandera)
print("\n  BFS")
bfs(grafo, raiz, bandera)
print("\n ")
print(f"Tiempo en ejcucion dfs: {tiempo_dfs} nanosegundos")
print(f"Tiempo en ejcucion bfs: {tiempo_bfs} nanosegundos")
print(f"Memoria dfs: {memoria_dfs} KB")
print(f"Memoria bfs: {memoria_bfs} KB")