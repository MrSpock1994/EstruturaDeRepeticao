"""
Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele
que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não
um número primo.

"""

n = int(input("Digite um numero inteiro: "))
divisores = []
for c in range(1, n+1, 1):
    if n % c == 0:
        divisores.append(c)
if len(divisores) == 2:
    print(f"{n} é um numero primo.")
else:
    print(f"{n} não é um numero primo.")