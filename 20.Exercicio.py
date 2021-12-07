"""
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias
vezes e limitando o fatorial a números inteiros positivos e menores que 16.


"""

while True:
    n = int(input('Digite o numero que deseja calcular o fatorial: '))
    if n >= 16:
        print('Você digitou um numero maior ou igual a 16, programa encerrado.')
        break
    lista = []
    multi = 1
    for c in range(1, n + 1):
        lista.append(c)

    for c in range(len(lista)):
        multi = lista[c] * multi

    print(f'O fatorial do numero desejado vale {multi}')
    lista.clear()
    outro = input('Deseja calcular fatorial de outro numero? S/N: ').strip().upper()
    if outro == 'N':
        print('Programa encerrado.')
        break
    if outro not in 'SN':
        print('Opcao invalida, programa encerrado.')
        break
