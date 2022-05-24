# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna

'''
Escribir un programa que pida al usuario un número entero positivo y
muestre por pantalla todos los números impares desde 1 hasta ese 
número separados por comas.
'''
from __future__ import print_function

numero = int(raw_input("Escribe un numero "))
digito = 1


while digito <= numero:
    if digito < numero-1:
    	print(digito, end=",")
    	pass
    else:
    	print(digito)
    
    digito = digito+2
    pass
