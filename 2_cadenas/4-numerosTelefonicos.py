# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna
'''
 Los teléfonos de una empresa tienen el siguiente formato
 prefijo-número-extension donde el prefijo es el código del país
 +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
 Escribir un programa que pregunte por un número de teléfono con este
 formato y muestre por pantalla el número de teléfono sin el prefijo
 y la extensión.
'''

numero = raw_input("Ingresa el numero telefonico.")

print numero[4:13]

#para impimir el segmento de un arreglo o alguna otra estructura de
#datos se usa [inicio:fin]