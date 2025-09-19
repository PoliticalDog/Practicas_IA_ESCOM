import random as ran

#Instrucciones
#Proponer una metodologia similar al append pero de python
#Se propone un listado con un dato inicial de 5 y se le pregunta al usaurio si desea agregar mas
#El listado debe ser unidimensional

def insertar(lista, caracter_nuevo):

    # se crea la lista con tamaño 2
    nueva_lista = [0] * (len(lista) + 1)

    # se copia de lista -> lista nueva
    for i in range(len(lista)):
        nueva_lista[i] = lista[i]
    nueva_lista[len(lista)] = caracter_nuevo #recorremos el nuevo valor al final

    return nueva_lista

#EJECUCION
lista = [5]
print(f"Lista inicial: {lista}")
opcion = 1 #variable del while
while opcion == 1:
    nuevo_elemento = int(input("Valor a agregar(numero): "))
    lista = insertar(lista, nuevo_elemento)
    print(f"Lista actualizada: {lista}")

    #Parametros para seguir
    print("1. SI")
    print("2. Salir")
    opcion = int(input("Quieres continuar?: "))
    print("\n")

print("Fin")