# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna

'''
Escribir un programa que pregunte al usuario una cantidad a invertir,
el interés anual y el número de años, y muestre por pantalla el capital
obtenido en la inversión cada año que dura la inversión.
'''

inversion = float(raw_input("Cuanto vas a invertir "))
interesAnual = float(raw_input("Interes anual: "))
aniosInversion = int(raw_input("Años de inversion: "))


for x in range(aniosInversion):
    capital = (interesAnual * inversion) / 100
    inversion = capital + inversion
    print "Año-",x+1,"--", round(inversion,2)
    pass