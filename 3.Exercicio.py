"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';

"""

nome = input('Digite seu nome: ').strip()
while len(nome) <= 3:
    print("Nome não permitido, gentileza tentar novamente abaixo:")
    nome = input('Digite seu nome: ').strip()
    if len(nome) > 3:
        print("Nome validado! ")
        break

idade = int(input("Digite sua idade: "))
while idade not in range(0, 151):
    print("Idade não permitida, gentileza tentar novamente abaixo:")
    idade = int(input("Digite sua idade: "))
    if 0 <= idade <= 150:
        print("Idade validada!")
        break

salario = int(input("Digite seu salario: "))
while salario < 0:
    print("Salario não permitido, gentileza tentar novamente abaixo:")
    salario = int(input("Digite seu salario: "))
    if salario > 0:
        print("Salario validado!")
        break

sexo = input('Digite a primeira letra referente ao seu sexo - [M/F]: ').lower().strip()
sexlist = ['f', 'm']
while sexo not in sexlist:
    print("Sexo não permitido, gentileza tentar novamente abaixo:")
    sexo = input('Digite a primeira letra referente ao seu sexo - [M/F]: ').lower().strip()
    if sexo in sexlist:
        print("Sexo validado!")
        break

print("Tabela para estado civil")
print()
print("Solteiro   ---- [1]")
print("Casado     ---- [2]")
print("Divorciado ---- [3]")
print("Viuvo      ---- [4]")
print()
civil = int(input('Escolha seu estado civil com base no código 1, 2, 3 ou 4: '))
estados = [1, 2, 3, 4]
while civil not in estados:
    print("Estado civil não permitido, gentileza tentar novamente abaixo:")
    civil = int(input('Escolha seu estado civil com base no código 1, 2, 3 ou 4: '))
    if civil in estados:
        print("Estado civil validado!")
        break
if sexo == 'f':
    sex = 'Female'
if sexo == 'm':
    sex = 'Male'
estado_civil = ['Solteiro', 'Casado', 'Divorciado', 'Viuvo']
resul = {'Name': nome, 'Age': idade, 'Salary': salario, 'Gender': sex, 'Civil': estado_civil[civil-1]}
print(resul)
