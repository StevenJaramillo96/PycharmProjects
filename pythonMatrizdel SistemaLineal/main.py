import numpy as np
# MATRIZ DEL SISTEMA LINEAL:
A=np.array([[6,0,0,0],[3,6,0,0],[4,-2,7,0],[5,-3,9,21]])
#Terminos Independientes
b=np.array([12,-12,14,-2])
#NUMERO DE ECUACIONES
n=np.size(b)
# Vector para almacenar la solucion
x=np.zeros(n)

# Sustitucion Progresiva
for i in range (n):
    sumj=0
    for j in range (i):
        sumj+=A[i,j]*x[j]
    x[i]=(b[i]-sumj)*1/A[i,i]
print(x)