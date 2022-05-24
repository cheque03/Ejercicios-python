# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna

'''
Escribir un programa que almacene la cadena de caracteres contraseña
en una variable, pregunte al usuario por la contraseña e imprima por
pantalla si la contraseña introducida por el usuario coincide con la
guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
'''

password = "contraseña"

contrasenia = raw_input("Igresa tu contraseña ")

if password == contrasenia.lower():
    print "son iguales"
else:
    print "son diferentes"
