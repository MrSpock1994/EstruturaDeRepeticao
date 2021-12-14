"""

Faça um programa que calcule o mostre a média aritmética de N notas.

"""

n = int(input("Digite a quantidade de notas a serem inseridas: "))
nota = 1
lista_notas = []
while nota <= n:
    c = float(input(f"Digite a {nota}° nota: "))
    lista_notas.append(c)
    nota += 1
print(f"As notas inseridas foram: {lista_notas}\n")
print(f"A media das notas inseridas é: {(sum(lista_notas)) / len(lista_notas)}")