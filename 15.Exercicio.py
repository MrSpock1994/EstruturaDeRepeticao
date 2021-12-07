"""
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.

"""

n = int(input('Digite a quantidade de termos que deseja ver: '))

x = 0
ordem = 0
lista = [1, 1]
while x < (n-2):
    c = lista[0 + ordem] + lista[1 + ordem]
    lista.append(c)
    ordem += 1
    x += 1
print(lista)
