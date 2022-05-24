# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna

'''
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo
al sexo y el nombre. El grupo A esta formado por las mujeres con un
nombre anterior a la M y los hombres con un nombre posterior a la N y
el grupo B por el resto. Escribir un programa que pregunte al usuario
su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
'''

nombre = raw_input("Escribe tu nombre ")
sexo = raw_input("Escribe tu sexo (h/m) ")


if sexo.lower() == 'm':
    if nombre[0].lower() <= 'm':
        print "Grupo A"
    else:
        print "Grupo B"
    pass
elif(sexo.lower() == 'h'):
    if nombre[0].lower() <= 'm':
        print "Grupo B"
        pass
    else:
        print "Grupo A"
