# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna

'''
Escribir un programa que muestre por pantalla la tabla de multiplicar
del 1 al 10.
'''
from __future__ import print_function

contador = 1
for contador in range(10):
    contador = contador + 1
    print(("--Tabla del --", contador), end="\n")
    for x in range(10):
        print(contador, " x ", (x + 1), " = ", (contador * (x+1)))
        pass
    pass

print("----Segunda opcion----")

for x in range(1,11):
	for j in range(1, 11):
		print(x*j, end="\t")
		pass
	print("")
	pass
