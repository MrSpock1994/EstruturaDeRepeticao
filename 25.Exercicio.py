"""
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma
varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada

"""

idades = []
p = 1
while True:
    n = int(input(f'Digite a idade da {p}° pessoa: \n'))
    idades.append(n)
    add = str(input('Deseja adicionar outra outra idade? [S/N]: ')).upper().strip()
    p += 1
    if add not in "SN":
        print("Opção invalida, programa finalizado!")
        break
    if add == 'N':
        print("Programa finalizado, até mais!")
        break

media = sum(idades) / len(idades)
if media <= 25:
    print(f'A media de idades é {media}, portando a turma é jovem.')
if 25 < media <= 60:
    print(f'A media de idades é {media}, portando a turma é adulta.')
if media > 60:
    print(f'A media de idades é {media}, portando a turma é idosa.')