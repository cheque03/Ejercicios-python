# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna

'''
Escribir un programa que pregunte al usuario su edad y muestre por
pantalla si es mayor de edad o no.
'''

edad = int(raw_input("Cual estu edad: "))

if edad >= 18:
    print "Eres mayor de edad"
    pass
else:
    print "No eres mayor de edad"
