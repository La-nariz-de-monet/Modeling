#!#/usr/bin/env python3

from sympy import *

x = Symbol("x") # Definimos x como simbolo

#Abrir archivo con la formula
with open("model.dat","r") as f:
    formulae = f.readline() #Leemos la formula en nuestro archivo



#formulae = 'x^3+1.0+sin(x)' # Definimos la función 

# Esto ya no es str sino es una función simbolica en la
# que x es un simbolo 
y = sympify(formulae) # Hacemos la función simbolica

# Tomamos la función y 
"""
.diff es el operador derivada y lo que le pasamos como 
argumento es respecto a lo que vamos a derivar
en este caso es x, derivamos respecto a x
"""
yprime = y.diff(x)

print (y)
print (yprime)

# lambdify lo que hace es tomar 
# y como función y su evaluación respecto a x
# evaluar con numpy 
"""
lambdifit toma una expresión simbolica y la vuelve una función 
cuyo equivalente es algo como: 
    def f(x):
        y = 2*x**2
        return(y)
"""
f = lambdify(x,y,"numpy")
# Evaluamos en determinado valor
x0 = 1.5
y0 = f(x0)

print(y0)

f1 = lambdify(x,yprime,"numpy")
y1 = f1(x0)
print(y1)
