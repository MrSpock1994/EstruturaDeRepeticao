"""
Faça um programa que peça 10 números inteiros, calcule e mostre a
quantidade de números pares e a quantidade de números impares.

"""

numeros = []
numeros_pares = []
numeros_impares = []
n = 0
while n < 10:
    num = int(input(f'Digite o {n + 1}° numero: '))
    numeros.append(num)
    if num % 2 == 1:
        numeros_impares.append(num)
    if num % 2 == 0:
        numeros_pares.append(num)
    n += 1

print(f'Lista de todos os numeros digitados {numeros}')
print()
print(f'Foram digitados {len(numeros_pares)} numeros pares.')
print()
print(f'Foram digitados {len(numeros_impares)} numeros impares.')