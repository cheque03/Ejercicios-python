# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna

'''
Escribir un programa para una empresa que tiene salas de juegos
para todas las edades y quiere calcular de forma automática el precio
que debe cobrar a sus clientes por entrar. El programa debe preguntar
al usuario la edad del cliente y mostrar el precio de la entrada. Si
el cliente es menor de 4 años puede entrar gratis, si tiene entre 4
y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
'''

'''
preguntar la edad
si es menor de 4 años
  entra gratis
si el cliente tiene en tre 4 y 18
  debe de pagar 5 euros
si el cliente es mayor de 18 años
  debe de pagar 10 euros '''

edad = int(raw_input("Escribe tu Edad "))

if edad < 4:
    print "entrada gratis"
elif edad <= 18:
    print "5 euros de entrada"
elif edad > 18:
    print "entrada 10 euros"
