# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna
'''
 Escribir un programa que pregunte el nombre completo del usuario en
 la consola y después muestre por pantalla el nombre completo del 
 usuario tres veces, una con todas las letras minúsculas, 
 otra con todas las letras mayúsculas y otra solo con la primera 
 letra del nombre y de los apellidos en mayúscula. El usuario puede
 introducir su nombre combinando mayúsculas y minúsculas como quiera.
'''

nombre = raw_input("Ingresa tu nombre completo")

print nombre.upper()
print nombre.lower()
print nombre.title()

