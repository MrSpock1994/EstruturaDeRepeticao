"""
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1.

"""
n = int(input('Digite um numero: '))
divisores = []
c = 1
while c <= n:
    if n % c == 0:
        divisores.append(c)
    c += 1
if len(divisores) > 2:
    print(f'O numero {n} não é primo.')
if len(divisores) == 2:
    print(f'O numero {n} é primo.')