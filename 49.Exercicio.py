"""
Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
Imprima no final a soma da série.

"""
from fractions import Fraction


n = int(input("Digite a quantidade de termos: "))
c = 1
s = 0
x = 1
serie = []
while c <= n:
    a = c / x
    w = str(Fraction(a).limit_denominator())
    serie.append(w)
    s += a
    c += 1
    x += 2

print(' + '.join(serie))
print(f"A soma da serie acima é {round(s, 2)}")
