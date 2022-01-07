"""
Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
  12376489
  => 98467321

"""

n = str(input("Digite um numero inteiro positivo: "))
inver = []
for c in range(len(n) - 1, -1, -1):
    inver.append(n[c])
print(''.join(inver))