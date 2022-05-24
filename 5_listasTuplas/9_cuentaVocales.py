# -*- encoding: utf-8 -*-
# !/usr/bin/env python
# codificado por: Ezequiel Ibarra Luna


'''
Escribir un programa que pida al usuario una palabra y muestre por
pantalla el número de veces que contiene cada vocal.
'''

palabra = raw_input("Escribe una palabra ")
vocales = ['a','e','i','o','u']

#opcion 1
for a in vocales:
    print a,"--", palabra.count(a)

#opcion 2
for vocal in vocales:
    cont = 0
    for letra in palabra:
        if letra == vocal:
            cont += 1
    print "La vocal " + vocal + " aparece " + str(cont) + "veces"