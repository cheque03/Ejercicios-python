# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna

'''
Escribir un programa que lea un entero positivo, , introducido por el
usuario y después muestre en pantalla la suma de todos los enteros
desde 1 hasta N. La suma de los primeros enteros positivos puede ser
calculada de la siguiente forma:
'''

numero = int(input("Escribe un numero: "))

total = ((numero*(numero+1))/2)
print 'la suma de 1 hasta el numero', numero, "es:", total
