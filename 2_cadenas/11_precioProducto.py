# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna
'''
Escribir un programa que pregunte el nombre el un producto, su precio
y un número de unidades y muestre por pantalla una cadena con el nombre
del producto seguido de su precio unitario con 6 dígitos enteros y 2
decimales, el número de unidades con tres dígitos y el coste total con
8 dígitos enteros y 2 decimales.
'''


print "### LIsta de Precios ### "

producto = raw_input("Escribe el nombre de un producto: ")
precio = float(raw_input("Escribe el precio de un producto: "))
cantidad = float(raw_input("Escribe la cantidad de un producto: "))
total = precio * cantidad
print "Producto: ", producto
print "precio unitario: ", "{:09.2f}".format(precio)
print "No unidades: ", "{:03.0f}".format(cantidad)
print "total: ", "{:0{}.{}f}".format(total, 11, 2)
