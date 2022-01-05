"""
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em
cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

"""

valores = []
qtd = int(input("Digite a quantidade de CDs: "))
a = 1
while a <= qtd:
    valores.append(float(input(f"Digite o valor do {a}° CD: ")))
    a += 1

print(f"O valor total investido foi de {sum(valores)} reais.\n")
print(f"O valor medio foi de {sum(valores)/qtd}")