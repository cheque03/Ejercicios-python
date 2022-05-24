# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna

'''
Escribir un programa que pida al usuario un número entero y muestre por
pantalla si es un número primo o no.
'''

numero = int(raw_input("Escribe un numero mayor  a 2:  "))

'''¿Cómo se sabe si un número es primo?
Los números primos son aquellos números naturales que solamente se pueden 
dividir por sí mismos y por 1, es decir, que si intentamos dividirlos por 
cualquier otro número, el resultado no es entero. 
El número 1 sólo tiene un divisor, que es él mismo, por eso no es 
considerado como un número primo. '''
i = 2
print numero % i
while numero % i != 0:
    print "while", numero, "%", i, "!= 0:"
    i += 1
    print i, "+= 1\n"
if i == numero:
    print "if", i, "==", numero,":"
    print numero, "Es primo"
else:
    print numero, "No es primo"





