import numpy as np        #Forma de Frobenius
from math import sqrt
# Matriz de A:
A=np.array([[7,1,-1,2],[1,8,0,-2],[-1,0,4,-1],[2,-2,-1,6]])
m=A.shape[0]    #Numero de Filas
n=A.shape[1]        #Numero de Columnas
sum_raiz=0
for i in range(m):
    for j in range(n):
        sum_raiz+=pow(A[i][j],2)
    Res=sqrt(sum_raiz)
print(round(Res,6))

