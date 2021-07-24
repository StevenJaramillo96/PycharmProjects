import numpy as np       # Metodo Jacobi
A=np.array([[7,1,-1,2],[1,8,0,-2],[-1,0,4,-1],[2,-2,-1,6]])
b=np.array([3,-5,4,-3])
k=15
n=A.shape[1]
D=np.eye(n)
D[np.arange(n),np.arange(n)]=A[np.arange(n),np.arange(n)]
LU=D-A
L=np.tril(LU)
U=np.triu(LU)
x=np.zeros(n)
print("  ",0,"vector Inicial:",x)
for i in range(k):
    D_inv=np.linalg.inv(D)
    x=np.dot(np.dot(D_inv,L+U),x)+np.dot(D_inv,b)
    print(" ",i+1,"El resultado de la iteracion es:",x.round(decimals=4))

