# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna
'''
 Escribir un programa que pregunte el nombre del usuario en la consola
 y un número entero e imprima por pantalla en líneas distintas el
 nombre del usuario tantas veces como el número introducido.
'''

nombre = raw_input("Escribe tu nombre ")
numero = int(raw_input("Ingresa un numero "))
print (nombre + "\n") * numero
