# -*- encoding: utf-8 -*-
# !/usr/bin/env python
# codificado por: Ezequiel Ibarra Luna


'''
Escribir un programa que almacene en una lista los siguientes precios,
50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor
de los precios.
'''

precios = [50, 75, 46, 22, 80, 65, 8]
precio, pp, nmin, nmax = 0,0,0,0

for x in precios:
    if precio > x:
        nmin = x
    precio = x
    if x > pp:
        nmax = x
    pp = x
    
print nmin, nmax

prices = [50, 75, 46, 22, 80, 65, 8]
min = max = prices[0]
print min, "=", max, "=", prices[0]

for price in prices:
    print "for", price, "in", prices,":"
    if price < min:
        print "\t if", price, "<", min,":"
        min = price
        print "\t\t", min, "=", price
    elif price > max:
        print "\telif", price, ">", max,":"
        max = price
        print "\t\t", max, "=", price
    print "----"


print "----"
print max(precios), min(precios)