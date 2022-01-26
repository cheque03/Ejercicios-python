# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna

'''
Escribir un programa que pregunte al usuario una cantidad a invertir,
el interés anual y el número de años, y muestre por pantalla el 
capital obtenido en la inversión.
'''

cantidad = float(raw_input('Ingresa una cantidad '))
interesAnual = float(raw_input('Ingresa el interes Anual(%) '))
numeroAnios = float(raw_input('Años de inversion '))
porcentaje = (interesAnual/100)*cantidad

capitalObtenido = (cantidad * numeroAnios) + (porcentaje * numeroAnios)

print "Capital obtenido", capitalObtenido
