"""
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue
pedindo até que o usuário informe um valor válido.

"""

n = int(input('Digite uma nota entre zero e dez: '))
if 0 <= n <= 10:
    print(f"A nota é: {n}")
while n > 10 or n < 0:
    print("A nota informada é inválida, gentileza informar novamente abaixo.")
    n = int(input('Digite uma nota válida: '))
    if 0 <= n <= 10:
        print(f"A nota é: {n}")
        break
