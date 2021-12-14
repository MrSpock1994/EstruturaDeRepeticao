"""
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato

"""
import  time
eleitores = int(input('Digite o numero total de eleitores: '))
candidato_1 = []
candidato_2 = []
candidato_3 = []
candidatos = [1, 2, 3]
n = 1
print("Bem vindo ao programa de eleição!\n")
while n <= eleitores:
    print('Note abaixo tabela para escolha dos candidatos.\n')
    print('1° Candidato ----- João ----- 1')
    print('2° Candidato ----- Pedro----- 2')
    print('3° Candidato ----- Marcos---- 3')
    print()
    print('Para escolher um candidato basta digitar o número referente ao candidato; 1, 2 ou 3.\n')
    print(f'{n}° eleitor, escolha seu voto abaixo.')
    c = int(input('Digite o número do candidato que deseja: \n'))
    print('Aguarde, computando voto.....')
    time.sleep(1)
    if c not in candidatos:
        print('O número informado não corresponde a nenhum candidato, o programa será encerrado!')
        break
    if c == 1:
        candidato_1.append(c)
    if c == 2:
        candidato_2.append(c)
    if c == 3:
        candidato_3.append(c)
    n += 1

print(f'Tivemos {eleitores} eleitores.\n')
print(f'O candidato João obteve {len(candidato_1)} votos.\n')
print(f'O candidato Pedro obteve {len(candidato_2)} votos.\n')
print(f'O candidato Marcos obteve {len(candidato_3)} votos.\n')
resultado = [len(candidato_1), len(candidato_2), len(candidato_3)]
mais_votos = max(resultado)
indice = resultado.index(mais_votos)
if indice == 0:
    print(f'O candidato João ganhou as eleições com {len(candidato_1)} votos.')
if indice == 1:
    print(f'O candidato Pedro ganhou as eleições com {len(candidato_2)} votos.')
if indice == 2:
    print(f'O candidato Marcos ganhou as eleições com {len(candidato_3)} votos.')