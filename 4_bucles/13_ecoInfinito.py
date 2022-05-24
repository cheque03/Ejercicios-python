# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna

'''
Escribir un programa que muestre el eco de todo lo que el usuario
introduzca hasta que el usuario escriba “salir” que terminará.
'''

print "salir termina el programa"
palabra = ""
while palabra != "salir":
	palabra = raw_input("Escribe una palabra ")
	print palabra
	pass

