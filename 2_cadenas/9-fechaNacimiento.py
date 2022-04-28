# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna
'''
Escribir un programa que pregunte al usuario la fecha de su nacimiento
en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
Adaptar el programa anterior para que también funcione cuando el día o
el mes se introduzcan con un solo carácter.
'''

fechaNacimiento = raw_input("Ingresa tu fecha de nacimiento( dd/mm/aaaa )")

print "dia", fechaNacimiento[:2]
print "mes", fechaNacimiento[3:5]
print "Año", fechaNacimiento[6:]
print "--------------"
print "Dia", fechaNacimiento[:fechaNacimiento.find('/')]
print "Mes", fechaNacimiento[fechaNacimiento.find('/')+1:-5]
print "Año", fechaNacimiento[-4:]
