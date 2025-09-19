#COMPLETA
#10) Dada la regresion de Ride
# a) Early stop y que imprima la cantidad de épocas que requirió para hacer el parámetro elegido <Ep, siempre que esté por debajo de las épocas max
# b) Implementar una normalización dif a las vistas en clase

import numpy as np
import matplotlib.pyplot as plt

def valor_absoluto(x):
    if x < 0:
        return -x
    else:
        return x

def maximo(lista):
    max_valor = lista[0]
    for i in lista:
        if i > max_valor:
            max_valor = i
    return max_valor

#Drfinicion de los hiperparametross
#x = np.array([2015,2016,2017,2018,2019,2020,2021,2022,2023])
x = np.array([1.0,3.0,6.0,9.0,11.0,15.0,16.0,19.0,24.0])
#Data set)
yd = np.array([4.0,5.0,6.5,7.0,8.5,12.0,13.0,16.0,22.0])

#normalizacion maximo absoluto
#   x / |x(max)|
# b) normalizacion valor_absoluto
max_x = maximo([valor_absoluto(i) for i in x])
max_yd = maximo([valor_absoluto(i) for i in yd])
x_norm = x / max_x
yd_norm = yd / max_yd

lr = 0.00001
#epocas = 1000
epocas = 20000
b0 = 0.1 ##Se recomienda inicializador entre 0 y 1 de forma random
b1 = 0.1

lamda=0.01 #penalizacion a b1 para evitar overfitting
m = len(x)
grafica = []

# a) Early stop
tope = 0.000001
error_anterior = float('inf')
contador_epocas = 0

for epoch in range(epocas):
  yobt = b0 + b1 * x_norm

  #calcular el ECM
  J = (1/(2*m))*np.sum((yd_norm - yobt)**2)+(lamda/2)*(b1**2)
  grafica +=[J]

  #Calcular de B0 y B1
  b0 = b0 - (lr/m)*np.sum(yobt-yd_norm)
  b1 = b1 - (lr/m)*np.sum((yobt-yd_norm)*x_norm)+(lamda/m)*b1
  #Early stopping
  if valor_absoluto(error_anterior - J) < tope:
        print(f"Se alcanzo el Early stop en la epoca {epoch}")
        contador_epocas = epoch
        break
  error_anterior = J

if contador_epocas == 0:
    contador_epocas = epocas

print(f"parametro BO={b0}")
print(f"parametro B1={b1}")
print(f"Epocas totales utilizadas: {contador_epocas}")

# Data Test
x_test = float(input("ingresa el valor de x:"))
x_test_norm = x_test / max_x
y_test = b0+b1*x_test_norm
print(f"El valor de y es:{y_test * max_yd}")

#clasificacion
test_clas_x=float(input("clasificacion eje x:"))
test_clas_y=float(input("clasificacion eje y:"))
test_clas_x_norm = test_clas_x / max_x
test_clas_y_norm = test_clas_y / max_yd

y_obt_class = b0+b1*test_clas_x_norm
if y_obt_class < test_clas_y_norm:
    print("Es clase 0 por encima de la recta")
else:
    print("Es clase 1 por debajo de la recta")

#Graficar J
plt.figure(figsize=(8,6))
plt.plot(range(len(grafica)),grafica,label="Funcion de coostos")
if contador_epocas < len(grafica): #verifica si hubo tope de Early stop
    plt.scatter(contador_epocas, grafica[contador_epocas], color='red', label=f'Tope alcanzado en la epoca {contador_epocas}')

plt.xlabel ("epocaa")
plt.ylabel ("J")
plt.title ("Comportamiento J")
plt.legend()
plt.show()

#Graficar los datos
plt.figure(figsize=(8,6))
for i in range(m):
  plt.scatter(x[i],yd[i])
x_val = [min(x), max(x)]
y_val = [(b0 + b1 * (xi / max_x)) * max_yd for xi in x_val]
plt.plot(x_val, y_val)
plt.scatter(test_clas_x, test_clas_y, color='green', marker='x', s=100, label='Clasificacion ingresada')
plt.legend()
plt.show()