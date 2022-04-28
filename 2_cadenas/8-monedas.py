# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna
'''
Escribir un programa que pregunte por consola el precio de un producto
en euros con dos decimales y muestre por pantalla el número de euros y
el número de céntimos del precio introducido.
'''

moneda = raw_input("Ingresa el precio del producto (00.00)")

print moneda[:moneda.find('.')], "euros y ", moneda[moneda.find('.')+1:], 'centimos'
#find() encuentra la primera aparicion del valor especificado al 
#agregar +1 al find le estamos adelantando una posicion 
print "Euros ", moneda[:2], "\n centimos: ", moneda[3:]
