# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna


'''
Escribir un programa que almacene en una lista los números del 1 al 10
y los muestre por pantalla en orden inverso separados por comas.
'''
from __future__ import print_function

numero = [1,2,3,4,5,6,7,8,9,10]
numero.reverse()
print ("ff", numero)

print ("---")

numero1 = [1,2,3,4,5,6,7,8,9,10]
for x in numero1[::-1]:
    print(x,end=" ")
    pass
print ("\n")