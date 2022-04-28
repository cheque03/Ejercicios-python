# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna
'''
Escribir un programa que pregunte el correo electrónico del usuario en
la consola y muestre por pantalla otro correo electrónico con el mismo
nombre (la parte delante de la arroba @) pero con dominio ceu.es.
'''

correo = raw_input("Ingresa tu correo ")

print correo[:correo.find('@')] + '@ceu.es'
