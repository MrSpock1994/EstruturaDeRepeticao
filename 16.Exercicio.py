"""
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,...
Faça um programa que gere a série até que o valor seja maior que 500.

"""

x = c = 0
ordem = 0
lista = [1, 1]
while c < 500:
    c = lista[0 + ordem] + lista[1 + ordem]
    lista.append(c)
    ordem += 1
    x += 1
print(lista)
