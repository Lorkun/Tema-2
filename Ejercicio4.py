#Algoritmo Iterativo Seca
import math

def funcion(x):
    return math.exp(-x) -x

def secante(x0,x1,t):
    while abs(x1-x0)> t:
        x2 = x1-funcion(x1)*(x1-x0)/(funcion(x1)-funcion(x0))
        x0 = x1
        x1 = x2

    return x2

print (secante(1,2,0 ))

#Algoritmo Iterativo Bis
import math

def funcion(x):
    return math.exp(-x) -x

def biseccion(a,b,t):
    if funcion(a)*funcion(b)> 0:
        print("No es posible")
    else:
        while abs(b-a)> t:
            c=(a+b)/2
            if funcion(a)*funcion(c)<0:
                b=c
            else:
                a = c
        return c

print (biseccion(1,2,0 ))

#Algoritmo Iterativo Newton-Raphson

import math

def funcion(x):
    return math.exp(-x) -x

def df(x):
    return math.exp(-x) -1

def newton(x0,t):
        while abs(funcion(x0))> t:
            x0 = x0 - funcion(x0)/df(x0)
        return x0

print (biseccion(1,2,0 ))


#Comparacion

import math

def funcion(x):
    return math.exp(-x) -x

def df(x):
    return math.exp(-x) -1

def newton(x0,t):
        while abs(funcion(x0))> t:
            x0 = x0 - funcion(x0)/df(x0)
        return x0

def biseccion(a,b,t):
    if funcion(a)*funcion(b)> 0:
        print("No es posible")
    else:
        while abs(b-a)> t:
            c=(a+b)/2
            if funcion(a)*funcion(c)<0:
                b=c
            else:
                a = c
        return c

def secante(x0,x1,t):
    while abs(x1-x0)> t:
        x2 = x1-funcion(x1)*(x1-x0)/(funcion(x1)-funcion(x0))
        x0 = x1
        x1 = x2

    return x2



print("Newton-Raphson:", newton(1,3))
print("Secante::", secante(1,2,3))
print("Biseccion:", biseccion(1,2,3))
