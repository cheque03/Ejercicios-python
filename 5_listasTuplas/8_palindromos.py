# -*- encoding: utf-8 -*-
# !/usr/bin/env python
# codificado por: Ezequiel Ibarra Luna


'''
Escribir un programa que pida al usuario una palabra y muestre por
pantalla si es un palíndromo.
'''

palabra = raw_input("Escribe una palabra: ")
inversa = palabra[::-1]
if inversa == palabra:
    print "La palabra ingresada es palindroma ", inversa
else: 
    print "No es palindroma ", inversa
