# Diseñe un código que encuentre el sen (pi/3) a través del desarrollo de Taylor,truncar cuando n=50
import numpy as pn
x=pn.pi/3
n= 51      #Lo hacemos hasta n=51, porque se empieza en cero
polinomio=0
print()
print("n   |     Pn(x)")
for k in  range(n):
    polinomio=polinomio + (-1)**k*x**(2*k+1) /pn.math.factorial(2*k+1)
    print(k,polinomio)

# Steven Jaramillo