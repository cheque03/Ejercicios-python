# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna

'''
Escribir un programa que pida al usuario un número entero y muestre
por pantalla un triángulo rectángulo como el de más abajo, de altura
el número introducido.

*
**
***
****
*****

'''

altura = int(raw_input("Ingresa la altura del triangulo "))
asterisco = "*"

for x in range(altura):
    print asterisco * (x + 1)
