# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna

'''
Escribir un programa que pida al usuario dos números enteros y muestre
por pantalla la <n> entre <m> da un cociente <c> y un resto <r>
donde <n> y <m> son los números introducidos por el usuario,
y <c> y <r> son el cociente y el resto de la división entera respectivamente.
'''

numero1 = int(raw_input("Escribe un numero:"))
numero2 = int(raw_input("Escribe un segundo numero:"))
total = numero1/numero2
resto = numero1%numero2
print ' ', numero1, 'y', numero2, 'da un cociente ', total, 'y un resto de ', resto
