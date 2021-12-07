"""
Faça um programa que, dado um conjunto de N números, determine o menor valor,
o maior valor e a soma dos valores.

Supondo conjunto aleatorio entre 0 e 1000
"""

import random

n = int(input('Digite a quantidade de termos do conjunto: '))
lista = []
while len(lista) < n:
    lista.append(random.randint(1, 1000))
print(lista)
print(f'O menor valor do conjunto é {min(lista)}\n')
print(f'O maior valor do conjunto é {max(lista)}\n')
print(f'A soma de todos os valores é {sum(lista)}')