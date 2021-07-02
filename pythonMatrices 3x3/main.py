import numpy as np
# Método sustitucion regresiva-Realizar Matriz 3x3 del sistema A
A=np.array([[1,2,-2],[0,1,-1],[0,0,1]])
# Terminos independientes
b=np.array([5,2,0])
#Hallar el numero de ecuaciones
n=np.size(b)
# Definir un vector para almacenar la solucion
x=np.zeros(n)
# El bucle que va ha ir de la ultima ecuacion hasta la primera
for i in range(n-1,-1,-1):
    sumj=0
    for j in range(i+1,n):
        sumj+=A[i,j]*x[j]
    x[i]=(b[i]-sumj)*1/A[i,i]
print(x)