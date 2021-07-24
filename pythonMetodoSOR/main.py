import numpy as np        #Metodo SOR
A=np.array([[7,1,-1,2],[1,8,0,-2],[-1,0,4,-1],[2,-2,-1,6]])
b=np.array([3,-5,4,-3])
k=5
w=1.1
n=A.shape[1]
D=np.eye(n)      # Matriz Identidad
D[np.arange(n),np.arange(n)]=A[np.arange(n),np.arange(n)]  # Matriz Diagonal
LU=D-A
L=np.tril(LU)
U=np.triu(LU)
D_wL=D-w*L
x=np.zeros(n)
print(" ",0,"Vector Inicial:",x)
for i in range (k):
    D_wL_inv=np.linalg.inv(D_wL)
    x=np.dot(np.dot(D_wL_inv,(1-w)*D+w*U),x)+w*np.dot(D_wL_inv,b)
    print(" ",i+1,"El resultado de iterar es:",x.round(decimals=4))