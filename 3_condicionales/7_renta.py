# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna

'''
Los tramos impositivos para la declaración de la renta en un
determinado país son los siguientes:

	Renta 	         Tipo impositivo
Menos de 10000€ 	    5%
Entre 10000€ y 20000€ 	15%
Entre 20000€ y 35000€ 	20%
Entre 35000€ y 60000€ 	30%
Más de 60000€ 	45%

Escribir un programa que pregunte al usuario su renta anual y muestre
por pantalla el tipo impositivo que le corresponde.
'''

renta = int(raw_input("Escribe tu renta Anual "))
impositivo = True
if renta > 60000:
	print "El impositivo es de el 45%"
	pass
elif  renta <= 60000 and renta > 35000:
    print "El impositivo es de el 30%"
elif renta <= 35000 and renta > 20000: 
	print "El impositivo es de el 20%"
elif renta <= 20000 and renta > 10000:
    print "El impositivo es de el 15%"
elif renta <= 10000:
	print "El impositivo es de el 5%"
