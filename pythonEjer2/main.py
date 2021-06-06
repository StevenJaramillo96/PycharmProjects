# Metodos Numericos/-Ejercico 2-Calcular la inversa de matrices de dimensión 2x2
print("Ingrese los elementos de la matriz: a, b, c, d")
a=float(input("Ingrese el valor de a :"))
b=float(input("Ingrese el valor de b :"))
c=float(input("Ingrese el valor de c :"))
d=float(input("Ingrese el avlor de d :"))

# Procedemos a encontrar el determinante
detA=a*d-b*c
#print(detA)
if(a*d-b*c==0):
    print("No hay inversa de la matriz A")  # Se mostrara este mensaje si no existe matriz inversa
else:
     a1=(1/detA)*d
     b1=(1/detA)*(-b)
     c1=(1/detA)*(-c)
     d1=(1/detA)*a
     print("La matriz inversa es:", [a1,b1],[c1,d1])

