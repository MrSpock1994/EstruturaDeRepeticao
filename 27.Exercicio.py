"""
Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a
quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

"""


alunos = []

n = int(input("Digite a quantidade de turmas: "))
c = 0
while c < n:
    a = int(input(f"Digite a quantidade de alunos da {c+1}° turma: "))
    if a > 40:
        print("As turmas não podem ter mais de 40 alunos!!")
        break
    alunos.append(a)
    c += 1
print(f"O numero medio de alunos por turma é de {sum(alunos) / n} alunos. ")

