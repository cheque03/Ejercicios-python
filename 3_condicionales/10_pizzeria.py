# !/usr/bin/env python
# -*- coding: utf-8 -*-
# codificado por: Ezequiel Ibarra Luna

'''
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas
a sus clientes. Los ingredientes para cada tipo de pizza aparecen a
continuación.

    Ingredientes vegetarianos: Pimiento y tofu.
    Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza
vegetariana o no, y en función de su respuesta le muestre un menú con
los ingredientes disponibles para que elija. Solo se puede eligir un
ingrediente además de la mozzarella y el tomate que están en todas la
pizzas. Al final se debe mostrar por pantalla si la pizza elegida es
vegetariana o no y todos los ingredientes que lleva.
'''
'''
preguntar al usuario el tipo de pizza
v=gegetarian nv=novegeteriana
si elige vegetariana
   mostrar ingredientes 1pimiento y 2tofu
      si elige 1pimiento
        imprimir vegetariana pimiento mozzarella y tomate
      si elige 2tofu
        imprimir vegetariana 2tofu mozzarella y tomate
si elige noVegetariana
   mostar ingredientes 1Peperoni, 2Jamón y 3Salmón
      si elige 1Peperoni
         imprimir noVegetariana mozzarella y tomate
      si elige 2Jamon
         imprimir noVegetariana mozzarella y tomate
      si elige 3Salmón
         imprimir4 noVegetariana mozzarella y tomate
fin del programa '''

tipoPizza = int(raw_input("Que pizza prefiere \n\t 1=Vegetariana \n\t 2=No Vegetariana \n"))
ingredientesDefault = "mozzarella y tomate"
vegetariana = 1
noVegetariana = 2

if tipoPizza == vegetariana:
    ingredientesVegetariana = int(raw_input("Elige un ingrediente \n\t 1=Pimiento \n\t 2 = tofu \n "))
    pimiento = 1
    tofu = 2
    if ingredientesVegetariana == pimiento:
        print "Elegiste Vegetariana que lleva pimiento, ", ingredientesDefault 
    elif ingredientesVegetariana == tofu:
        print "Elegiste Vegetariana que lleva tofu con, ", ingredientesDefault 
    else:
    	print "Opcion no valida"
elif tipoPizza == noVegetariana:
    ingreNoVegetariana = int(raw_input("Elige un ingrediente \n\t 1=Peperoni \n\t 2=Jamón \n\t 3=Salmón\n "))
    peperoni = 1
    jamon = 2
    salmon = 3
    if ingreNoVegetariana == peperoni:
    	print "\n Su pizza es No Vegetariana lleva Peperoni, ", ingredientesDefault
    	pass
    elif ingreNoVegetariana == jamon:
    	print "\n Su pizza es No Vegetariana lleva Jamon, ", ingredientesDefault
    elif ingreNoVegetariana == salmon:
    	print "\n Su pizza es No Vegetariana lleva Salmon, ", ingredientesDefault
    else:
    	print "Opcion no valida"
else:
	print "opcion no valida"