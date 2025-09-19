import tracemalloc as mem
import time as tm
import random as ran

"""
Práctica 1
1) Ingresar cualquier grafo
2) Generar un número aleatorio entero dentro del rango del número de nodos
3) Para BFS Y DFS cuando encuentre la bandera se detenga el programa
4) Medir tiempo y memoria (compare ambos algoritmos)
"""

tiempo_dfs= None
tiempo_bfs=None
memoria_dfs=None
memoria_bfs=None

#def = funcion
def dfs(grafo, nodo_raiz, bandera):
    global tiempo_dfs, memoria_dfs      #globales para comparacion
    #cronometro y memoria
    start_time = tm.time_ns()
    mem.start()

    #inicio de variables
    previo = [nodo_raiz]                    ##Arreglo
    visitados = [False] * (len(grafo) + 1)  #arreglo visitados
    visitados[nodo_raiz] = True             #false

    i = 0 #indice mi pila de previos
    #while i < len(previo) and  bandera_encontrada_dfs==False:
    while previo:
        #nodo_actual, *previo = previo
        nodo_actual = previo.pop()  # Cambia aquí si quieres usar una cola, sería `pop(0)`
        if nodo_actual == nodo_raiz:
            print(f"Raíz {nodo_actual}")
            print("  |")
        elif nodo_actual == bandera:
            print(f"Se llegó al nodo '{nodo_actual}' destino con DFS")
            break
        else:
            print(f"  {nodo_actual}")
            print("  |")

        #recorremos nodos hijos  -->Reversded para inverit el sentido horario
        for vecino in reversed(grafo[nodo_actual]):  # Invertimos el sentido
        #for vecino in grafo[nodo_actual]:
            if not visitados[vecino]:
                visitados[vecino] = True
                previo.append(vecino)
                #previo.append(vecino) #Eliminar append, es nativo de python
        i = i + 1

    end = tm.time_ns()
    tiempo_dfs = end - start_time
    print(f"Tiempo de ejecución: {tiempo_dfs} nanosegundos")    #tiempo
    current, peak = mem.get_traced_memory()                     # memoria
    mem.stop()
    memoria_dfs = current
    print(f"Memoria de ejecución: {memoria_dfs} KB")



def bfs(grafo, nodo_raiz, bandera):
    global tiempo_bfs, memoria_bfs
    #Cronometro y memoria
    start_time = tm.time_ns()
    mem.start()

    #inicio de variables
    previo = [nodo_raiz]
    visitados = [False] * (len(grafo) + 1)
    visitados[nodo_raiz] = True

    i=0
    while i < len(previo):
        #nodo_actual = previo.pop(0)            # cambiar pop por otra fuuncion
        nodo_actual, *previo = previo

        if nodo_actual == nodo_raiz:
            print(f"Raiz {nodo_actual}")
            print("  |")
        elif nodo_actual == bandera:
            print(f"Se llego al nodo '{nodo_actual}' destino con bfs")
            break
        else:
            print(f"  {nodo_actual}")
            print("  |")

        # recorremos nodos hermanos
        for vecino in grafo[nodo_actual]:
            if not visitados[vecino]:
                visitados[vecino] = True
                previo = previo + [vecino]
                #previo.append(vecino)          #cambiar append por otra opcion

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
raiz = 2
print(f"\nEl nodo raiz es: {raiz} ")
bandera = ran.randint(1,8)
if bandera == raiz:
    bandera = ran.randint(1,8)
    print(f"El nodo bandera generado aleatorio fue: {bandera} ")
else:
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