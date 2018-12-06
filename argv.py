# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 20:41:41 2018

@author: Fabricio
"""

import sys

print('Todos los argumentos pasados en la linea de comandos:', sys.argv)

print('El nombre del script Python que se esta ejecutando actualmente es ', sys.argv[0])

print('\n\n**** Programa para multiplicar dos numeros****\n\n')

numero1 = sys.argv[1]
numero2 = sys.argv[2]

try:
    numero1 = float(numero1)
    numero2 = float(numero2)
    total = numero1 * numero2
    print('El total de la multimplicacion de ', numero1, ' por ', numero2, ' es igual a ', total)
except ValueError:
    print ('Error los argumentos para multiplicar han de ser numericos')
    
    


