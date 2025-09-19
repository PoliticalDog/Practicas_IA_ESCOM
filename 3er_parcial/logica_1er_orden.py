#9 Realizar con lógica de 1er orden, la solución de dados únicamente en
# la base de conocimiento las relaciones padre-hijo de al menos 10 parejas. Determinar quien es abuelo de quien y quien es tio de quien

import numpy as np

#base conmocimeinto padre e hijo
relaciones = [
    ["Carlos", "Juan"],
    ["Carlos", "Ana"],
    ["Luis", "Pedro"],
    ["Luis", "Maria"],
    ["Juan", "Sofia"],
    ["Juan", "Diego"],
    ["Ana", "Lucas"],
    ["Ana", "Sara"],
    ["Pedro", "Luisito"],
    ["Maria", "Elena"]
]

def encontrar_abuelos(relaciones):
    abuelos = []
    for padre, hijo in relaciones:
        for posible_abuelo, padre_actual in relaciones:
            if padre == padre_actual:  # Si el padre del hijo tiene un padre
                abuelos += [[posible_abuelo, hijo]]
    return abuelos

def encontrar_tios(relaciones):
    tios = []
    for padre, hijo in relaciones:
        for posible_tio, sobrino_padre in relaciones:
            if padre != posible_tio and padre in [r[1] for r in relaciones if r[0] == posible_tio]:  # Si comparten un abuelo
                tios += [[posible_tio, hijo]]
    return tios

#EJECUCION
abuelos = encontrar_abuelos(relaciones)
tios = encontrar_tios(relaciones)

# IMPRESION
print("Relaciones de abuelos:")
for abuelo in abuelos:
    print(f"{abuelo[0]} es abuelo(a) de {abuelo[1]}")

print("\nRelaciones de tios:")
for tio in tios:
    print(f"{tio[0]} es tio(a) de {tio[1]}")

