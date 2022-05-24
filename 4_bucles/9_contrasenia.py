# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna

'''
Escribir un programa que almacene la cadena de caracteres contraseña
en una variable, pregunte al usuario por la contraseña hasta que 
introduzca la contraseña correcta.
'''


texto = ""
cadena = "contraseña"

while texto != cadena:
    texto = raw_input("Ingresa la contraseña ")
    pass
print "Haz atinado la contraseña"

