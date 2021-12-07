"""

Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
Mostre a soma dos números.


"""

a = int(input('Digite o primeiro número inteiro: '))
b = int(input('Digite o segundo número inteiro: '))

numeros = []
if a < b:
    for n in range(a+1, b):
        print(n)
        numeros.append(n)
if b < a:
    for n in range(b+1, a):
        print(n)
        numeros.append(n)
if b == a:
    print('Os números sao iguais.')

print(f'A soma dos numeros é {sum(numeros)}')