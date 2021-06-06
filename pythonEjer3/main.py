# Ejercicio3 # Graficar las siguientes funciones en la misma grafica
import numpy as np                      #Importamos librerias
import matplotlib.pyplot as plt
# coordenadas en eje x
x=np.arange(0,10,0.2)
x1=np.arange(1.2,10,0.2)
# coordenadas en el eje y
f1=x**2-x+1
g=2/(x1-1)

#Trazar las funciones
#plt.plot(x,f1)
#plt.plot(x1,g)
#plt.show()

plt.subplot(2,1,1)
plt.plot(x,f1)
plt.title("Funcion Cuadratica")
plt.xlabel("x")
plt.ylabel("y")

plt.subplot(2,1,2)
plt.plot(x1,g)
plt.title("Funcion Racional")
plt.show()