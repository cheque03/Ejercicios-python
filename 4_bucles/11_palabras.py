# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna

'''
Escribir un programa que pida al usuario una palabra y luego muestre
por pantalla una a una las letras de la palabra introducida empezando
por la última.
'''

palabra = raw_input("Ingresa una palabra: ")

for  x in palabra[::-1]:
	print x
	pass
