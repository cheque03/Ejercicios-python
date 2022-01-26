# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna

'''
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
calcule el índice de masa corporal y lo almacene en una variable, y muestre
por pantalla la frase Tu índice de masa corporal es <imc> donde <imc>
es el índice de masa corporal calculado redondeado con dos decimales.
'''

peso = float(raw_input("ingresar su peso (kg)"))
estatura = float(raw_input("Ingresa tu estatura (m)"))
masaCorporal = (peso/(estatura**2))
print "Tu indice de masa corporal es:",round(masaCorporal,2)
