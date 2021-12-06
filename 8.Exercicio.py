"""

Faça um programa que leia 5 números e informe a soma e a média dos números.
"""

numeros = []

for n in range(1, 6):
    nu = int(input(f'Digite o {n}° numero: '))
    numeros.append(nu)

soma = sum(numeros)
media = soma / len(numeros)

print(f'A soma dos números digitados é: {soma}')
print()
print(f'A média dos numeros digitados é: {media}')