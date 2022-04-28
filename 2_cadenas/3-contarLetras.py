# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna
'''
 Escribir un programa que pregunte el nombre del usuario en la consola
 y después de que el usuario lo introduzca muestre por pantalla
 <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en
 mayúsculas y <n> es el número de letras que tienen el nombre.
'''

nombre = raw_input("Escribe tu nombre ")
ss = '''Hola 
desde un texto 
multilinea'''

print ss
print nombre.upper(), "tiene ", len(nombre), "letras"
