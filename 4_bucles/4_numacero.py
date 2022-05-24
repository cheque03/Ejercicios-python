# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna

'''
Escribir un programa que pida al usuario un número entero positivo
y muestre por pantalla la cuenta atrás desde ese número hasta cero
separados por comas.
'''

from __future__ import print_function

numero  = int(raw_input("Escibe un numero "))


for i in range(numero, 1-1, -1):
    print(i,end="'")

