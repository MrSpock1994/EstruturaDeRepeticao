"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120.

"""

n = int(input("Digite o numero que deseja ver o fatorial: "))
b =1
for c in range(n, 0, -1):
    b *= c
print(f"Fatorial de {n}:\n")
print(f"{n}! = {b}")
