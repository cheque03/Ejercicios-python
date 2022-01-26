# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna

'''
Una juguetería tiene mucho éxito en dos de sus productos:
payasos y muñecas. Suele hacer venta por correo y la empresa
de logística les cobra por peso de cada paquete así que deben
calcular el peso de los payasos y muñecas que saldrán en cada
paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g.
Escribir un programa que lea el número de payasos y muñecas
vendidos en el último pedido y calcule el peso total del paquete
que será enviado.
'''

payaso = 112
munieca = 75

nPayasos = int(raw_input("numero de payasos vendioos "))
nMuniecas = int(raw_input("numeor de muñecas vendidas "))

peso = (nPayasos * payaso) + (nMuniecas * munieca)

print 'El peso del paquete es: ', peso, 'gramos'

