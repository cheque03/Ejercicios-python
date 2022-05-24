# -*- encoding: utf-8 -*-
# !/usr/bin/env python
# codificado por: Ezequiel Ibarra Luna


'''
Escribir un programa que almacene el abecedario en una lista,
elimine de la lista las letras que ocupen posiciones múltiplos de 3,
y muestre por pantalla la lista resultante.

Un número es múltiplo de 3 cuando es el resultado de multiplicar 3 por otro número.
'''


abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', \
              'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',\
              'V', 'W', 'X', 'Y', 'Z']
abc3 = []
multiplo = 0
for x in abecedario:
    while abecedario.index(x) == multiplo:
        abc3.append(x)
        multiplo += 3
for x in abc3:
    abecedario.remove(x)
    pass
print abecedario
