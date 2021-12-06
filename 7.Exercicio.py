"""
Faça um programa que leia 5 números e informe o maior número.

"""

numeros = []

for n in range(0,5):
    nu = int(input('Digite um número: '))
    numeros.append(nu)

maximo = max(numeros)
print(f'O maior valor digitado foi {maximo}')