# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna

'''
Una panadería vende barras de pan a 3.49€ cada una. 
El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de barras vendidas
que no son del día. Después el programa debe mostrar el precio habitual
de una barra de pan, el descuento que se le hace por no ser fresca y 
el coste final total.
'''

precio = float(3.49)
desc = float(40)
precioAnterior = (desc/100)*precio


panVendido = float(raw_input("No de barras vendidas del dia anterior "))
print precio, " descuento de 60% ", precioAnterior * panVendido
