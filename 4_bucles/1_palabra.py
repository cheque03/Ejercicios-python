# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna

'''
Escribir un programa que pida al usuario una palabra y la muestre por
pantalla 10 veces.
'''

palabra = raw_input("Escribe una palabra ")
contador = 1
print "\t",palabra * 10

for i in range(10):
	print i, "--", palabra
	pass
# while contador <= 10 :
# 	print contador, "--", palabra
# 	contador=contador+1
# 	pass