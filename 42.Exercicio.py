"""
Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes
intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.

"""
lista1 = []
lista2 = []
lista3 = []
lista4 = []

while True:
    print("Caso deseje sair do programa, basta digitar um numero negativo.\n")
    n = int(input("Digite um numero inteiro: "))
    if 0 <= n <= 25:
        lista1.append(n)
    if 26 <= n <= 50:
        lista2.append(n)
    if 51 <= n <= 75:
        lista3.append(n)
    if 76 <= n <= 100:
        lista4.append(n)
    if n < 0:
        break
print(f"Temos {len(lista1)} números entre [0-25], {lista1}\n ")
print(f"Temos {len(lista2)} números entre [26-50], {lista2}\n ")
print(f"Temos {len(lista3)} números entre [51-75], {lista3}\n ")
print(f"Temos {len(lista4)} números entre [76-100], {lista4}\n ")