# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna

'''
Escribir un programa que pida al usuario un número entero y muestre
por pantalla un triángulo rectángulo como el de más abajo.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
'''
from __future__ import print_function

numero = int(raw_input("Escribe un numero "))
for y in range(1,numero+2,2):
    for x in range(y,-1, -2):
        print(x,end=" ")
        pass
    print(" ")
    pass

