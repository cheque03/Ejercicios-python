# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna


'''
Escribir un programa que pregunte al usuario los números ganadores de
la lotería primitiva, los almacene en una lista y los muestre por 
pantalla ordenados de menor a mayor.
'''

loteria = []

while len(loteria)+1 <= 6 :
	numero = int(raw_input("Ingresa un valor entre 1 y 49 : "))
	if numero >=1 and numero <= 49:
		loteria.append(numero)
	else:
		print "El numero debe de ser menor a 49"
loteria.sort()
print loteria
