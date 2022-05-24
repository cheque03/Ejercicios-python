# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna

'''
Para tributar un determinado impuesto se debe ser mayor de 16 años y
tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir
un programa que pregunte al usuario su edad y sus ingresos mensuales y
muestre por pantalla si el usuario tiene que tributar o no.
'''


edad = int(raw_input("ingresa tu edad "))
ingreso = int(raw_input("Ingresos mensuales "))

if (edad > 16) and (ingreso > 1000):
    print "Te toca tributar "
else:
    print "no tributaras"
