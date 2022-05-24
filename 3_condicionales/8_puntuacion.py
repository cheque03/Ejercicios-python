# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna

'''
En una determinada empresa, sus empleados son evaluados al final de
cada año. Los puntos que pueden obtener en la evaluación comienzan en
0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los
puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o 
más, pero no valores intermedios entre las cifras mencionadas. 
A continuación se muestra una tabla con los niveles correspondientes a
cada puntuación. La cantidad de dinero conseguida en cada nivel es de
2.400€ multiplicada por la puntuación del nivel.

Nivel 	Puntuación
Inaceptable 	0.0
Aceptable 	0.4
Meritorio 	0.6 o más

Escribir un programa que lea la puntuación del usuario e indique su 
nivel de rendimiento, así como la cantidad de dinero que recibirá el
usuario.
''' 
'''
si la puntuacion es igual a 0.0
  imprimir inaceptable y
  multiplicar 0.0 por 2400
  e imprimir el resultado
entoncessi la puntuacion es igual 0.4
  imprimir Aceptable y
  multiplicar 0.4 por 2400
  e imprimir el resultado
entonces si la puntuacion es mayor o igual a 0.6
  imprimir Meritorio
  multiplicar puntuacion por 2400
  e imprimir el resultado '''

puntuacion = float(raw_input("Ingresa la puntuacion del usuario (0.0,\
                            0.4, 0.6 o más): "))
if puntuacion == 0.0:
	print "El nivel de rendimiento es inacetable el dinero recibira es de ", puntuacion*2400 
	pass
elif puntuacion == 0.4:
	print "El nivel de rendimiento es aceptable el dinero recibira es\
	       de ", puntuacion * 2400
elif puntuacion >= 0.6:
    print "El nivel de rendimiento es Meritorio el dinero que recibira\
    es de", puntuacion * 2400
else:
  print "valor ", puntuacion, "no valido"