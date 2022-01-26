# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna

'''
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece
el 4% de interés al año. Estos ahorros debido a intereses, que no se
cobran hasta finales de año, se te añaden al balance final de tu cuenta
de ahorros. Escribir un programa que comience leyendo la cantidad
de dinero depositada en la cuenta de ahorros, introducida por el
usuario. Después el programa debe calcular y mostrar por pantalla
la cantidad de ahorros tras el primer, segundo y tercer años. Redondear
cada cantidad a dos decimales.
'''

cantidad = float(raw_input("Cantidad ahorrada "))
interes = float(4)

totalAnio1 = ((interes/100)*cantidad) + cantidad
totalAnio2 = ((interes/100)*totalAnio1) + totalAnio1
totalAnio3 = ((interes/100)* totalAnio2) + totalAnio2

print "Inversion del pimer año ", round(totalAnio1, 2)
print "Inversion del segundo año ", round(totalAnio2, 2)
print "Inversion del tercer año ", round(totalAnio3, 2)