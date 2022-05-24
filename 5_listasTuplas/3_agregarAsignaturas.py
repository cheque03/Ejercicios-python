# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna


'''
Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista, pregunte al usuario la nota que ha sacado en cada
asignatura, y después las muestre por pantalla con el mensaje 
En <asignatura> has sacado <nota> donde <asignatura> es cada una 
des las asignaturas de la lista y <nota> cada una de las 
correspondientes notas introducidas por el usuario.
'''

asignaturas = ['Matemáticas','Física','Química', 'Historia','Lengua']
calif = []
for x in asignaturas:
	nota = int(raw_input("Escribe la nota que sacaste en %s: " %x ))
	notas = x, nota
	calif.append(notas)
	pass
print "\n"
for asignatura,nota in calif:
	print "En",asignatura, "sacaste", nota
	pass

print "fin"

