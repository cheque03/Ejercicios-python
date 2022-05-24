# -*- encoding: utf-8 -*-
# !/usr/bin/env python
# codificado por: Ezequiel Ibarra Luna


'''
Escribir un programa que almacene las matrices
 
 A = 1 2 3     b = -1 2
     4 5 6          0 1
                    1 1

en una lista y muestre por pantalla su producto.
Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.
producto: el resultado de multiplicar a * b = c
el producto escalar se calcula como 
prodEscalar = a1 * b1 + a2*b2+ a3*b3
'''

v1 = (1,2,3)
v2 = (-1,0,2)
count = 0

for e in range(len(v1)):
    count += v1[e] * v2[e]

print count
