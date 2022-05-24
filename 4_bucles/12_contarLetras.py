# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna

'''
Escribir un programa en el que se pregunte al usuario por una frase y
una letra, y muestre por pantalla el número de veces que aparece la
letra en la frase.
'''

frase = raw_input("Escribe una Frase: ")
letra = raw_input("Escribe una letra: ")
contador = 0
for x in frase:
	if letra == x:
		contador += 1
	pass

print "la letra", letra, "se repite", contador 
