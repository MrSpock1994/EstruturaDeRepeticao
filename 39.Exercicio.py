"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno
mais alto e o número do aluno mais baixo, junto com suas alturas

"""

aluno = []
altura = []

for c in range(1, 4):
    aluno.append(int(input(f"Digite o numero do {c}° aluno: ")))
    altura.append(int(input(f"Digite a altura em cm do {c}° aluno: ")))

alto = max(altura)
baixo = min(altura)
i1 = altura.index(alto)
i2 = altura.index(baixo)

print(f"O aluno mais alto é o aluno {aluno[i1]} com uma altura de {alto} cm\n")
print(f"O aluno mais baixo é o aluno {aluno[i2]} com uma altura de {baixo} cm")