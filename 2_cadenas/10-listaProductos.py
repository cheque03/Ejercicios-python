# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna
'''
Escribir un programa que pregunte por consola por los productos de una
cesta de la compra, separados por comas, y muestre por pantalla cada
uno de los productos en una línea distinta.
'''

lista = raw_input("Ingresa una lista de productos separados por coma: ")

print lista.replace(',',' \n')