# -*- encoding: utf-8 -*-
# !/usr/bin/env python
# codificado por: Ezequiel Ibarra Luna


'''
Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una
lista, pregunte al usuario la nota que ha sacado en cada asignatura y
elimine de la lista las asignaturas aprobadas. Al final el programa 
debe mostrar por pantalla las asignaturas que el usuario tiene que 
repetir.
'''

asignaturas = ['Matematicas', 'Fisica', 'Quimica', 'Historia', 'Lengua']
repetir = []
for x in asignaturas:
    nota = int(raw_input("La nota que has sacado en %s: " %x))    
    if nota < 60:
        repetir.append(x)

print "Las asignaturas a repetir son: ", repetir
