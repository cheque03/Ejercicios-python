# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna

'''
Escribir un programa que pida al usuario un número entero y muestre
por pantalla si es par o impar.
'''

numero = int(raw_input("Escribe un numero "))

if numero % 2 == 0:
    print "es par"
else:
    print "es Impar"
