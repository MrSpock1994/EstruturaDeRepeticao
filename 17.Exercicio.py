"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

"""

n = int(input('Digite o numero que deseja calcular o fatorial: '))
lista = []
multi = 1
for c in range(1, n+1):
    lista.append(c)

for c in range(len(lista)):
    multi = lista[c] * multi

print(f'O fatorial do numero desejado vale {multi}')