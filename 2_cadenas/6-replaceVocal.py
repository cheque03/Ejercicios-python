# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna
'''
Escribir un programa que pida al usuario que introduzca una frase en
la consola y una vocal, y después muestre por pantalla la misma frase
pero con la vocal introducida en mayúscula.
'''

frase = raw_input("Ingresa una frase:  ")
vocal = raw_input("Ingresa la vocal a editar: ")

print "Frase inicial ", frase,"\nFrase modificada ", frase.replace(vocal,\
vocal.upper())