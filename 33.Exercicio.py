"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto
indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas,
bem como a média das temperaturas.

"""

temp = []
print("**********TEMPERATURAS*********")
while True:
    print("Informe a temperatura abaixo, caso deseje sair do programa basta digitar 'S'.")
    t = str(input("Digite a temperatura: "))
    if t in "sS":
        break
    t = int(t)
    temp.append(t)
print(f"A maior temperatura é {max(temp)}.")
print()
print(f"A menor temperatura é {min(temp)}.")
print()
print(f"A media de temperatura foi {sum(temp)/len(temp)}")