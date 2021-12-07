"""

Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
O usuário deve informar de qual numero ele deseja ver a tabuada.

"""

n = int(input('Deseja ver a tabuada de qual número?: '))

for c in range(1, 11):
    print(f'{n} X {c} = {n * c}')
