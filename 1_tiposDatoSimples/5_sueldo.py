# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna

'''
Escribir un programa que pregunte al usuario por el número de horas
trabajadas y el coste por hora. Después debe mostrar por pantalla
la paga que le corresponde.
'''


horas = int(raw_input("¿Cuantas horas trabajaste? "))
coste = int(raw_input("El costo de la hora es: "))
pago = horas * coste
print "Tu sueldo es de: ", pago
