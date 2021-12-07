"""
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

"""

n = int(input('Digite o limitante superior: '))
numeros = []
primos = []
x = 1
w = 0


def verifica_primo(z):
    divisores = []
    c = 1
    while c <= z:
        if z % c == 0:
            divisores.append(c)
        c += 1
    if len(divisores) == 2:
        primos.append(z)
    divisores.clear()


while x <= n:
    numeros.append(x)
    x += 1

for w in range(0, len(numeros)-1):
    verifica_primo(numeros[w])
print(primos)
print(len(primos))









